from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, ProfileSerializer, CounterSerializer, BuildingSerializer
from django.contrib.auth.models import User
from portal.models import UserProfile, Counter, Building



@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail' : 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token' : token.key, 'user' : serializer.data})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.username))


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def profile_counters(request):
    buildingsId = []
    profilesId =[]
    user_serializer = UserSerializer(instance=request.user)
    try:
        user_profile = UserProfile.objects.filter(user_id=request.user.id)
        print(user_profile)
    except:
        return Response({'detail' : 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    finally:
        print(user_profile)
    user_profile_serializer = ProfileSerializer(user_profile, many=True)
    # print(user_profile_serializer.data)
    for user in user_profile: #TODO: change to comprehention expression, unfourtenately [id for building_id in user_profile] doesn't work propper way
        buildingsId.append(user.building_id)
    try:
        building = Building.objects.filter(id__in = buildingsId)
        print(building)
    except:
        return Response({'detail' : 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    finally:
        building = BuildingSerializer(building, many=True)
    for user in user_profile: #TODO: change to comprehention expression, unfourtenately [id for building_id in user_profile] doesn't work propper way
        profilesId.append(user.id)
    try:
        user_profile_counters = Counter.objects.filter(profile_id__in = profilesId)
        print(user_profile_counters)
    except:
        return Response({'detail' : 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    finally:
        counters_serializer = CounterSerializer(user_profile_counters, many=True)
    return Response({'user' : user_serializer.data, 'profile': user_profile_serializer.data, 'building' : building.data, 'counters' : counters_serializer.data})


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def add_counter(request):
    print(request.data)
    serializer = CounterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)