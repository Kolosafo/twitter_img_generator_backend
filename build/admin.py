from django.contrib import admin
from .models import VerifiedVotes, ContactUs, TransactionReceipt,RealVoteCount

# Register your models here.
admin.site.register(VerifiedVotes)
admin.site.register(ContactUs)
admin.site.register(TransactionReceipt)
admin.site.register(RealVoteCount)
