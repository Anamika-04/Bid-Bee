from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Auction, Product, Bid
from django.views import generic
from app.forms import Bidding_Form
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def auctions(request):
    assert isinstance(request, HttpRequest)
    auction_list = Auction.objects.filter(time_ending__gte=datetime.now()).order_by('time_ending')
    product_list = Product.objects
    bid_list = Bid.objects
    if request.method == "POST":
        bid_form = Bidding_Form(request.POST)
        if bid_form.is_valid():
            amt = bid_form.cleaned_data['bid_amount']
            au_id = bid_form.cleaned_data['auction_id']
            
            if amt >= Auction.objects.get(id = au_id).start_price:
                bid = Bid(
                    user_id = User.objects.get(id = request.user.id),
                    bid_amount = amt,
                    bid_time = datetime.now(),
                    auction_id = Auction.objects.get(id = au_id)
                )
             
                bid.save()
            else:
                return HttpResponse("Bidding amount should be greater than starting price. Go back & try again!")
            bid_form = Bidding_Form()
    else:
        bid_form = Bidding_Form()
    
    return render(
        request,
        'app/auctions.html',
        {
            'title':'Auctions',
            'year':datetime.now().year,
            'auction_list': auction_list,
            'product_list': product_list,
            'bid_list': bid_list,
            'bid_form': bid_form
        }
    )
