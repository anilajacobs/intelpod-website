from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db import models
from .models import Product, Benefit, Testimonial, OrderItem
from .cart import Cart
from .forms import OrderForm, ContactForm


def home(request):
    """Home page view"""
    products = Product.objects.filter(available=True)[:6]
    benefits = Benefit.objects.filter(active=True)
    testimonials = Testimonial.objects.filter(active=True)[:6]

    context = {
        'products': products,
        'benefits': benefits,
        'testimonials': testimonials,
    }
    return render(request, 'products/home.html', context)


def product_list(request):
    """Product listing page"""
    products = Product.objects.filter(available=True)

    context = {
        'products': products,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    """Product detail page"""
    from .models import ProductReview, FAQ
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(available=True).exclude(id=product.id)[:4]

    # Get approved reviews
    reviews = ProductReview.objects.filter(product=product, approved=True)
    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
    review_count = reviews.count()

    # Get FAQs for this product
    faqs = FAQ.objects.filter(product=product, active=True) | FAQ.objects.filter(product=None, active=True)

    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),
        'review_count': review_count,
        'faqs': faqs[:10],  # Limit to 10 FAQs
    }
    return render(request, 'products/product_detail.html', context)


@require_POST
def cart_add(request, product_id):
    """Add product to cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart.add(product=product, quantity=quantity)
    messages.success(request, f'{product.name} has been added to your cart.')

    return redirect('cart_detail')


@require_POST
def cart_remove(request, product_id):
    """Remove product from cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'{product.name} has been removed from your cart.')

    return redirect('cart_detail')


def cart_detail(request):
    """Cart detail page"""
    cart = Cart(request)
    return render(request, 'products/cart.html', {'cart': cart})


def checkout(request):
    """Checkout page"""
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_amount = cart.get_total_price()
            if request.user.is_authenticated:
                order.user = request.user
            order.save()

            # Create order items
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )

            # Clear the cart
            cart.clear()

            messages.success(request, f'Your order #{order.order_number} has been placed successfully!')
            return redirect('order_success', order_number=order.order_number)
    else:
        form = OrderForm()

    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'products/checkout.html', context)


def order_success(request, order_number):
    """Order success page"""
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
    }
    return render(request, 'products/order_success.html', context)


def contact(request):
    """Contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'products/contact.html', context)


def about(request):
    """About page"""
    from .models import TeamMember
    team_members = TeamMember.objects.filter(active=True)
    context = {
        'team_members': team_members,
    }
    return render(request, 'products/about.html', context)


def blog_list(request):
    """Blog listing page"""
    from .models import BlogPost
    blog_posts = BlogPost.objects.filter(published=True)
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'products/blog_list.html', context)


def blog_detail(request, slug):
    """Blog post detail page"""
    from .models import BlogPost
    blog_post = get_object_or_404(BlogPost, slug=slug, published=True)
    # Get related posts (same author or recent)
    related_posts = BlogPost.objects.filter(published=True).exclude(id=blog_post.id)[:3]
    context = {
        'blog_post': blog_post,
        'related_posts': related_posts,
    }
    return render(request, 'products/blog_detail.html', context)


def privacy_policy(request):
    """Privacy Policy page"""
    return render(request, 'products/privacy_policy.html')
