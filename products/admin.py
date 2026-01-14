from django.contrib import admin
from .models import (
    Product, ProductImage, Feature, Benefit,
    Testimonial, Order, OrderItem, ContactMessage,
    BlogPost, ProductReview, FAQ, TeamMember
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    can_delete = False
    readonly_fields = ('product', 'quantity', 'price')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'created_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, FeatureInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'short_description', 'image')
        }),
        ('Pricing', {
            'fields': ('price', 'original_price')
        }),
        ('Inventory', {
            'fields': ('stock', 'available')
        }),
        ('Specifications', {
            'fields': ('height', 'length', 'width', 'material')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt_text', 'order']
    list_filter = ['product']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['product', 'title', 'order']
    list_filter = ['product']


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'active']
    list_editable = ['order', 'active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating', 'active', 'created_at']
    list_filter = ['rating', 'active', 'created_at']
    list_editable = ['active']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'get_customer_name', 'email',
                    'total_amount', 'status', 'paid', 'created_at')
    list_filter = ('status', 'paid', 'created_at')
    search_fields = ('order_number', 'email', 'first_name', 'last_name')
    readonly_fields = ('order_number', 'created_at', 'updated_at')
    inlines = [OrderItemInline]

    def get_customer_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_customer_name.short_description = 'Customer'

    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'status', 'total_amount', 'paid')
        }),
        ('Customer Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address', 'city', 'state', 'pincode', 'country')
        }),
        ('Payment Details', {
            'fields': ('payment_method', 'payment_id')
        }),
        ('Additional Information', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'subject', 'created_at']
    list_editable = ['read']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('read', 'created_at')
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'published']
    list_filter = ['published', 'published_date', 'author']
    list_editable = ['published']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['published_date', 'updated_at']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'author', 'featured_image', 'excerpt', 'content')
        }),
        ('Publishing', {
            'fields': ('published', 'published_date', 'updated_at')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )


class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'rating', 'created_at', 'approved']
    list_filter = ['approved', 'rating', 'created_at', 'product']
    list_editable = ['approved']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Review Information', {
            'fields': ('product', 'name', 'email', 'rating')
        }),
        ('Review Content', {
            'fields': ('title', 'comment')
        }),
        ('Status', {
            'fields': ('approved', 'created_at')
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'product', 'order', 'active', 'created_at']
    list_filter = ['active', 'product', 'created_at']
    list_editable = ['order', 'active']
    search_fields = ['question', 'answer']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'active']
    list_filter = ['role', 'active']
    list_editable = ['order', 'active']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'role', 'title', 'photo', 'bio')
        }),
        ('Contact', {
            'fields': ('email', 'linkedin_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'active')
        }),
    )
