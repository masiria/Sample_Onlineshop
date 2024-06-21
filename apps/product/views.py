from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from . import models
from .forms import CommentForm


class ProductDetailView(View):
    def get(self, request, product_slug):
        comment_form = CommentForm()
        product = get_object_or_404(models.Product, slug=product_slug, is_active=True)
        products_similar_tags = models.Product.objects.filter(tag__in=product.tag.all()).exclude(id=product.id)
        products_similar_category = models.Product.objects.filter(category=product.category).exclude(id=product.id)
        related_products = products_similar_category.intersection(products_similar_tags)[:4]

        attributes_values = models.ProductAttributeValue.objects.filter(product=product)
        context = {
            'product': product,
            'related_products': related_products,
            'attributes_values': attributes_values,
            'comment_form': comment_form
        }
        return render(request, 'product/product_detail.html', context)

    def post(self, request, product_slug):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = get_object_or_404(models.Product, slug=product_slug)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
        return HttpResponseRedirect(self.request.path_info)


class CategoryPageView(View):
    def get(self, request, category_slug):
        category = get_object_or_404(models.Category, slug=category_slug)
        products = models.Product.objects.filter(category=category, is_active=True)
        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'product/category.html', context=context)


class TagPageView(View):
    ...

