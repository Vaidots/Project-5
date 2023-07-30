from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    metal = None
    if 'product_metal' in request.POST:
        metal = request.POST['product_metal']
    bag = request.session.get('bag', {})

    if metal:
        if item_id in list(bag.keys()):
            if metal in bag[item_id]['items_by_metal'].keys():
                bag[item_id]['items_by_metal'][metal] += quantity
                messages.success(
                    request, f'Updated {metal.upper()} {product.name} \
                        quantity to {bag[item_id]["items_by_metal"][metal]}')

            else:
                bag[item_id]['items_by_metal'][metal] = quantity
                messages.success(
                    request, f'Added {metal.upper()} \
                        {product.name} to your bag')

        else:
            bag[item_id] = {'items_by_metal': {metal: quantity}}
            messages.success(
                request, f'Added {metal.upper()} {product.name} to your bag')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')

        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    metal = None
    if 'product_metal' in request.POST:
        metal = request.POST['product_metal']
    bag = request.session.get('bag', {})

    if metal:
        if quantity > 0:
            bag[item_id]['items_by_metal'][metal] = quantity
            messages.success(
                request, f'Updated  {metal.upper()} {product.name} \
                    quantity to {bag[item_id]["items_by_metal"][metal]}')

        else:
            del bag[item_id]['items_by_metal'][metal]
            if not bag[item_id]['items_by_metal']:
                bag.pop(item_id)
                messages.success(
                    request, f'Removed  {metal.upper()}\
                         {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        metal = None
        if 'product_metal' in request.POST:
            metal = request.POST['product_metal']
        bag = request.session.get('bag', {})

        if metal:
            del bag[item_id]['items_by_metal'][metal]
            if not bag[item_id]['items_by_s']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed  {metal.upper()}\
                     {product.name} from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
