from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .design import apc_design, pdp_design, lp_design, nnpp_design, banner_design, post_design, post_3_design
import base64
import io
from .models import VerifiedVotes, ContactUs
import random


def single_img_base64_string(image):
    img_buffered = io.BytesIO()

    image.save(img_buffered, format="JPEG")
    base64_result = base64.b64encode(img_buffered.getvalue()).decode("utf-8")
    return base64_result


def pillow_image_to_base64_string(img_one, img_two):
    img_one_buffered = io.BytesIO()
    img_two_buffered = io.BytesIO()

    img_one.save(img_one_buffered, format="JPEG")
    img_two.save(img_two_buffered, format="JPEG")

    watermarked = base64.b64encode(img_one_buffered.getvalue()).decode("utf-8")
    original = base64.b64encode(img_two_buffered.getvalue()).decode("utf-8")
    return watermarked, original


# Create your views here.
@api_view(['POST'])
def design_profile(request):
    returnObj = {
        "watermarked": {
            "profile_img": "",
            "banner_img": "",
            "post_img": "",
            "post_3_img": ""
        },
        "original": {
            "profile_img": "",
            "banner_img": "",
            "post_img": "",
            "post_3_img": ""
        }

    }
    data = request.data
    profile_img = data["profile_img"]
    party = data["party"]
    name = data["name"]

    if(party == "APC"):
        wm_apc_img, og = apc_design(profile_img)
        wm_apc_banner_img, og_banner = banner_design(name, party)
        wm_apc_post_design, og_post = post_design(party, name, profile_img)
        wm_apc_post_3_design, og_post_3 = post_3_design(
            profile_img, name, "TEST INSPIRATION", party)

        wm_img_url, og_img_url = pillow_image_to_base64_string(wm_apc_img, og)
        wm_banner_url, og_banne_url = pillow_image_to_base64_string(
            wm_apc_banner_img, og_banner)
        wm_post_url, og_post_url = pillow_image_to_base64_string(
            wm_apc_post_design, og_post)
        wm_post_3_url, og_post_3_url = pillow_image_to_base64_string(
            wm_apc_post_3_design, og_post_3)

        returnObj["watermarked"]["profile_img"] = "data:image/jpeg;base64," + wm_img_url
        returnObj["watermarked"]["banner_img"] = "data:image/jpeg;base64," + wm_banner_url
        returnObj["watermarked"]["post_img"] = "data:image/jpeg;base64," + wm_post_url
        returnObj["watermarked"]["post_3_img"] = "data:image/jpeg;base64," + wm_post_3_url

        returnObj["original"]["profile_img"] = "data:image/jpeg;base64," + og_img_url
        returnObj["original"]["banner_img"] = "data:image/jpeg;base64," + og_banne_url
        returnObj["original"]["post_img"] = "data:image/jpeg;base64," + og_post_url
        returnObj["original"]["post_3_img"] = "data:image/jpeg;base64," + og_post_3_url

    elif(party == "PDP"):
        wm_pdp_img, og = pdp_design(profile_img)
        wm_pdp_banner_img, og_banner = banner_design(name, party)
        wm_pdp_post_design, og_post = post_design(party, name, profile_img)
        wm_pdp_post_3_design, og_post_3 = post_3_design(
            profile_img, name, "TEST INSPIRATION", party)

        wm_img_url, og_img_url = pillow_image_to_base64_string(wm_pdp_img, og)
        wm_banner_url, og_banne_url = pillow_image_to_base64_string(
            wm_pdp_banner_img, og_banner)
        wm_post_url, og_post_url = pillow_image_to_base64_string(
            wm_pdp_post_design, og_post)
        wm_post_3_url, og_post_3_url = pillow_image_to_base64_string(
            wm_pdp_post_3_design, og_post_3)

        returnObj["watermarked"]["profile_img"] = "data:image/jpeg;base64," + wm_img_url
        returnObj["watermarked"]["banner_img"] = "data:image/jpeg;base64," + wm_banner_url
        returnObj["watermarked"]["post_img"] = "data:image/jpeg;base64," + wm_post_url
        returnObj["watermarked"]["post_3_img"] = "data:image/jpeg;base64," + wm_post_3_url

        returnObj["original"]["profile_img"] = "data:image/jpeg;base64," + og_img_url
        returnObj["original"]["banner_img"] = "data:image/jpeg;base64," + og_banne_url
        returnObj["original"]["post_img"] = "data:image/jpeg;base64," + og_post_url
        returnObj["original"]["post_3_img"] = "data:image/jpeg;base64," + og_post_3_url

    elif(party == "LP"):
        wm_lp_img, og = lp_design(profile_img)
        wm_lp_banner_img, og_banner = banner_design(name, party)
        wm_lp_post_design, og_post = post_design(party, name, profile_img)
        wm_lp_post_3_design, og_post_3 = post_3_design(
            profile_img, name, "TEST INSPIRATION", party)

        wm_img_url, og_img_url = pillow_image_to_base64_string(wm_lp_img, og)
        wm_banner_url, og_banne_url = pillow_image_to_base64_string(
            wm_lp_banner_img, og_banner)
        wm_post_url, og_post_url = pillow_image_to_base64_string(
            wm_lp_post_design, og_post)
        wm_post_3_url, og_post_3_url = pillow_image_to_base64_string(
            wm_lp_post_3_design, og_post_3)

        returnObj["watermarked"]["profile_img"] = "data:image/jpeg;base64," + wm_img_url
        returnObj["watermarked"]["banner_img"] = "data:image/jpeg;base64," + wm_banner_url
        returnObj["watermarked"]["post_img"] = "data:image/jpeg;base64," + wm_post_url
        returnObj["watermarked"]["post_3_img"] = "data:image/jpeg;base64," + wm_post_3_url

        returnObj["original"]["profile_img"] = "data:image/jpeg;base64," + og_img_url
        returnObj["original"]["banner_img"] = "data:image/jpeg;base64," + og_banne_url
        returnObj["original"]["post_img"] = "data:image/jpeg;base64," + og_post_url
        returnObj["original"]["post_3_img"] = "data:image/jpeg;base64," + og_post_3_url

    elif(party == "NNPP"):
        wm_nnpp_img, og = nnpp_design(profile_img)
        wm_nnpp_banner_img, og_banner = banner_design(name, party)
        wm_nnpp_post_design, og_post = post_design(party, name, profile_img)
        wm_nnpp_post_3_design, og_post_3 = post_3_design(
            profile_img, name, "TEST INSPIRATION", party)

        wm_img_url, og_img_url = pillow_image_to_base64_string(wm_nnpp_img, og)
        wm_banner_url, og_banne_url = pillow_image_to_base64_string(
            wm_nnpp_banner_img, og_banner)
        wm_post_url, og_post_url = pillow_image_to_base64_string(
            wm_nnpp_post_design, og_post)
        wm_post_3_url, og_post_3_url = pillow_image_to_base64_string(
            wm_nnpp_post_3_design, og_post_3)

        returnObj["watermarked"]["profile_img"] = "data:image/jpeg;base64," + wm_img_url
        returnObj["watermarked"]["banner_img"] = "data:image/jpeg;base64," + wm_banner_url
        returnObj["watermarked"]["post_img"] = "data:image/jpeg;base64," + wm_post_url
        returnObj["watermarked"]["post_3_img"] = "data:image/jpeg;base64," + wm_post_3_url

        returnObj["original"]["profile_img"] = "data:image/jpeg;base64," + og_img_url
        returnObj["original"]["banner_img"] = "data:image/jpeg;base64," + og_banne_url
        returnObj["original"]["post_img"] = "data:image/jpeg;base64," + og_post_url
        returnObj["original"]["post_3_img"] = "data:image/jpeg;base64," + og_post_3_url
    else:
        return JsonResponse("Invalid Party", status=400)

    return JsonResponse(returnObj, status=200)


def updateViewCount():
    randomIncrease = random.randint(100, 800)
    try:
        verifiedVotes = VerifiedVotes.objects.get(pk=1)
        verifiedVotes.verified += randomIncrease
        verifiedVotes.save()
    except:
        pass

    return


@api_view(['GET'])
def getViewCount(request):
    verifiedVotes = VerifiedVotes.objects.get(pk=1)
    returnObj = {
        "votes": verifiedVotes.verified
    }
    return JsonResponse(returnObj, safe=False, status=200)


@api_view(['POST'])
def contactUs(request):
    try:
        data = request.data
        name = data["name"]
        message = data["message"]
    except Exception as E:
        print("EXPETPOO,", E)

    ContactUs.objects.create(name=name, message=message)
    return JsonResponse("Success", safe=False, status=200)
