from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from shoesshop.models import (
    Shoe,
    Product,
    Image,
    Clothes,
    Accessory,
    UserCartProduct,
    UserLoveProduct,
)
from shoesshop.serializer import (
    CartSerializer,
    LoveSerializer,
    ShoeSerializer,
    UserSerializer,
    ProductSerializer,
    ImageSerializer,
    UserCartProductSerializer,
    UserLoveProductSerializer,
    AccessorySerializer,
    ClothesSerializer,
)


class UserView(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, data):
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "User Created Successfully",
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "User updated Successfully!",
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(instance=user)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "user is invalid!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(
            {
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# # Cách 1: Ngắn gọn nhất
# class ShoeView(viewsets.ModelViewSet):
#     serializer_class = ShoeSerializer
#     queryset = Shoe.objects.all()

# -----------------------------upload image to cloud--------------------


class ImageView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        urls = []
        try:
            files = request.FILES.getlist("image")
            for f in files:
                upload_data = cloudinary.uploader.upload(f)
                urls.append(upload_data["url"])
            return Response(
                {
                    "message": "success",
                    "data": urls,
                },
                status=201,
            )
        except:
            return Response({"message": "error", "data": []}, status=400)

    def createImage(data):
        serializer = ImageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return

    def getListImage(idP):
        images = Image.objects.filter(product=idP)
        # serializer = ImageSerializer(instance=images, many=True)
        return images.values()


# -------------------------------Product view------------------------------------


class ProductView(viewsets.ViewSet):
    def createProduct(data):
        serializer = ProductSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return serializer["product_id"].value

    @api_view(["GET"])
    def getListProduct(self, page=None):
        try:
            page = page
            fistItem = (page - 1) * 12
            data = []
            products = Product.objects.all()[fistItem : fistItem + 12]
            for product in products:
                images = ImageView.getListImage(product.product_id)
                data.append(
                    {
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": product.price,
                        "salePercent": product.salePercent,
                        "in_stock": product.in_stock,
                        "sold": product.sold,
                        "images": images,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def searchProduct(self, page=None, key=None):
        try:
            page = page
            key = key
            fistItem = (page - 1) * 12
            data = []
            products = Product.objects.filter(name__contains=key)[
                fistItem : fistItem + 12
            ]
            for product in products:
                images = ImageView.getListImage(product.product_id)
                data.append(
                    {
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": product.price,
                        "salePercent": product.salePercent,
                        "in_stock": product.in_stock,
                        "sold": product.sold,
                        "images": images,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # filter by sale and price
    @api_view(["GET"])
    def filterProduct(request, page=None, sale=None, price=None):
        try:
            page, sale, price = page, sale, price
            fistItem = (page - 1) * 12
            data = []
            products = []
            # sale and asc price
            if sale == 1 and price == 1:
                products = Product.objects.filter(salePercent__gt=0).order_by("price")[
                    fistItem : fistItem + 12
                ]
            # sale and dsc price
            if sale == 1 and price == 2:
                products = Product.objects.filter(salePercent__gt=0).order_by("-price")[
                    fistItem : fistItem + 12
                ]
            # sale and not sort by price
            if sale == 1 and price == 0:
                products = Product.objects.filter(salePercent__gt=0)[
                    fistItem : fistItem + 12
                ]
            # not sale and asc price
            if sale == 0 and price == 1:
                print("zoooo")
                products = Product.objects.order_by("price")[fistItem : fistItem + 12]
            # not sale and dsc price
            if sale == 0 and price == 2:
                products = Product.objects.order_by("-price")[fistItem : fistItem + 12]
            for product in products:
                images = ImageView.getListImage(product.product_id)
                data.append(
                    {
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": product.price,
                        "salePercent": product.salePercent,
                        "in_stock": product.in_stock,
                        "sold": product.sold,
                        "images": images,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )


# -------------------------------Shoe view------------------------------------------


class ShoeView(viewsets.ViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()

    def retrieve(self, request, pk=None):
        try:
            shoe = Shoe.objects.get(pk=pk)
            images = ImageView.getListImage(shoe.product.product_id)
            product = {
                "product_id": shoe.product.product_id,
                "name": shoe.product.name,
                "price": shoe.product.price,
                "salePercent": shoe.product.salePercent,
                "in_stock": shoe.product.in_stock,
                "sold": shoe.product.sold,
                "image": images,
            }
            data = {
                "shoe_id": shoe.shoe_id,
                "gender": shoe.gender,
                "series": shoe.series,
                "shape": shoe.shape,
                "product": product,
            }
            # serializer = ShoeSerializer(instance=shoe)
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Shoe not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def getListShoe(self, page=None):
        try:
            page = page
            fistItem = (page - 1) * 12
            data = []
            shoes = Shoe.objects.all()[fistItem : fistItem + 12].select_related(
                "product"
            )
            for s in shoes:
                images = ImageView.getListImage(s.product.product_id)
                product = {
                    "product_id": s.product.product_id,
                    "name": s.product.name,
                    "price": s.product.price,
                    "salePercent": s.product.salePercent,
                    "in_stock": s.product.in_stock,
                    "sold": s.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "shoe_id": s.shoe_id,
                        "gender": s.gender,
                        "series": s.series,
                        "shape": s.shape,
                        "product": product,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "error",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def create(self, request, *args, **kwargs):
        try:
            product = ProductView.createProduct(request.data["product"])
            for img in request.data["image"]:
                image = {
                    "product": product,
                    "url": img["url"],
                    "is_thumbnail": img["is_thumbnail"],
                }
                ImageView.createImage(image)
            data = {
                "product": product,
                "gender": request.data["shoe"]["gender"],
                "series": request.data["shoe"]["series"],
                "shape": request.data["shoe"]["shape"],
            }
            serializer = ShoeSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Shoe Created Successfully!",
                },
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        shoe = Shoe.objects.get(pk=pk)
        serializer = ShoeSerializer(instance=shoe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "Shoe updated Successfully!",
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            Shoe.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "Shoe delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Shoe not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# -------------------------------Clothes view--------------------------------------
class ClothesView(viewsets.ViewSet):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            product = ProductView.createProduct(request.data["product"])
            for img in request.data["image"]:
                image = {
                    "product": product,
                    "url": img["url"],
                    "is_thumbnail": img["is_thumbnail"],
                }
                ImageView.createImage(image)
            data = {
                "product": product,
                "category": request.data["cloth"]["category"],
            }
            serializer = ClothesSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Cloth Created Successfully!",
                },
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            Clothes.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "Cloth delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cloth not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def retrieve(self, request, pk=None):
        try:
            cloth = Clothes.objects.get(pk=pk)
            images = ImageView.getListImage(cloth.product.product_id)
            product = {
                "product_id": cloth.product.product_id,
                "name": cloth.product.name,
                "price": cloth.product.price,
                "salePercent": cloth.product.salePercent,
                "in_stock": cloth.product.in_stock,
                "sold": cloth.product.sold,
                "image": images,
            }
            data = {
                "clothes_id": cloth.clothes_id,
                "category": cloth.category,
                "product": product,
            }
            # serializer = ShoeSerializer(instance=shoe)
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cloth not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def getListClothes(self, page=None):
        try:
            page = page
            fistItem = (page - 1) * 12
            data = []
            clothes = Clothes.objects.all()[fistItem : fistItem + 12].select_related(
                "product"
            )
            for c in clothes:
                images = ImageView.getListImage(c.product.product_id)
                product = {
                    "product_id": c.product.product_id,
                    "name": c.product.name,
                    "price": c.product.price,
                    "salePercent": c.product.salePercent,
                    "in_stock": c.product.in_stock,
                    "sold": c.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "clothes_id": c.clothes_id,
                        "category": c.category,
                        "product": product,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "error",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    # filter by sale, category, price
    @api_view(["GET"])
    def filterClothes(request, page=None, sale=None, category=None, price=None):
        try:
            page, sale, category, price = page, sale, category, price
            fistItem = (page - 1) * 12
            data = []
            clothes = []
            # sale
            if sale == 1:
                # have cate
                if category != 0:
                    if price == 1:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0, category=category
                        )[fistItem : fistItem + 12]
                # not have cate
                else:
                    if price == 1:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        clothes = Clothes.objects.filter(product__salePercent__gt=0)[
                            fistItem : fistItem + 12
                        ]
            # not sale
            else:
                # have cate
                if category != 0:
                    if price == 1:
                        clothes = Clothes.objects.filter(category=category).order_by(
                            "product__price"
                        )[fistItem : fistItem + 12]
                    if price == 2:
                        clothes = Clothes.objects.filter(category=category).order_by(
                            "-product__price"
                        )[fistItem : fistItem + 12]
                    if price == 0:
                        clothes = Clothes.objects.filter(category=category)[
                            fistItem : fistItem + 12
                        ]
                # not have cate
                else:
                    if price == 1:
                        clothes = Clothes.objects.all().order_by("product__price")[
                            fistItem : fistItem + 12
                        ]
                    if price == 2:
                        clothes = Clothes.objects.all().order_by("-product__price")[
                            fistItem : fistItem + 12
                        ]
            for c in clothes:
                images = ImageView.getListImage(c.product.product_id)
                product = {
                    "product_id": c.product.product_id,
                    "name": c.product.name,
                    "price": c.product.price,
                    "salePercent": c.product.salePercent,
                    "in_stock": c.product.in_stock,
                    "sold": c.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "clothes_id": c.clothes_id,
                        "category": c.category,
                        "product": product,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )


# ------------------------------Accessory view----------------------------------
class AccessoryView(viewsets.ViewSet):
    serializer_class = AccessorySerializer
    queryset = Accessory.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            product = ProductView.createProduct(request.data["product"])
            for img in request.data["image"]:
                image = {
                    "product": product,
                    "url": img["url"],
                    "is_thumbnail": img["is_thumbnail"],
                }
                ImageView.createImage(image)
            data = {
                "product": product,
                "category": request.data["accessory"]["category"],
            }
            serializer = AccessorySerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Accessory Created Successfully!",
                },
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            accessory = Accessory.objects.get(pk=pk)
            images = ImageView.getListImage(accessory.product.product_id)
            product = {
                "product_id": accessory.product.product_id,
                "name": accessory.product.name,
                "price": accessory.product.price,
                "salePercent": accessory.product.salePercent,
                "in_stock": accessory.product.in_stock,
                "sold": accessory.product.sold,
                "image": images,
            }
            data = {
                "accessory_id": accessory.accessory_id,
                "category": accessory.category,
                "product": product,
            }
            # serializer = ShoeSerializer(instance=shoe)
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Accessory not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            Accessory.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "Accessory delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Accessory not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    @api_view(["GET"])
    def getListAccessory(self, page=None):
        try:
            page = page
            fistItem = (page - 1) * 12
            data = []
            accessories = Accessory.objects.all()[
                fistItem : fistItem + 12
            ].select_related("product")
            for a in accessories:
                images = ImageView.getListImage(a.product.product_id)
                product = {
                    "product_id": a.product.product_id,
                    "name": a.product.name,
                    "price": a.product.price,
                    "salePercent": a.product.salePercent,
                    "in_stock": a.product.in_stock,
                    "sold": a.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "accessory_id": a.accessory_id,
                        "category": a.category,
                        "product": product,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "error",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    # filter by sale, category, price
    @api_view(["GET"])
    def filterAccessory(request, page=None, sale=None, category=None, price=None):
        try:
            page, sale, category, price = page, sale, category, price
            fistItem = (page - 1) * 12
            data = []
            accessories = []
            # sale
            if sale == 1:
                # have cate
                if category != 0:
                    if price == 1:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0, category=category
                        )[fistItem : fistItem + 12]
                # not have cate
                else:
                    if price == 1:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0
                        )[fistItem : fistItem + 12]
            # not sale
            else:
                # have cate
                if category != 0:
                    if price == 1:
                        accessories = Accessory.objects.filter(
                            category=category
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.filter(
                            category=category
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        accessories = Accessory.objects.filter(category=category)[
                            fistItem : fistItem + 12
                        ]
                # not have cate
                else:
                    if price == 1:
                        accessories = Accessory.objects.all().order_by(
                            "product__price"
                        )[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.all().order_by(
                            "-product__price"
                        )[fistItem : fistItem + 12]
            for a in accessories:
                images = ImageView.getListImage(a.product.product_id)
                product = {
                    "product_id": a.product.product_id,
                    "name": a.product.name,
                    "price": a.product.price,
                    "salePercent": a.product.salePercent,
                    "in_stock": a.product.in_stock,
                    "sold": a.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "clothes_id": a.clothes_id,
                        "category": a.category,
                        "product": product,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )


# -------------------------------USER CART PRODUCT VIEW -------------------------------------
class UserCartProductView(viewsets.ViewSet):
    queryset = UserCartProduct.objects.all()

    def list(self, request):
        user_id = request.query_params.get("user_id")
        if user_id is not None:
            cart = UserCartProduct.objects.filter(user_id=user_id)
        else:
            cart = UserCartProduct.objects.all()
        serializer = UserCartProductSerializer(instance=cart, many=True)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_404_NOT_FOUND,
        )

    def retrieve(self, request, pk=None):
        try:
            cart = UserCartProduct.objects.get(pk=pk)
            serializer = UserCartProductSerializer(instance=cart)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cart item not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def create(self, request):
        data = request.data
        serializer = CartSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "data": serializer.data,
                "message": "Cart item Created Successfully!",
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):
        cart = UserCartProduct.objects.get(pk=pk)
        serializer = CartSerializer(instance=cart, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "Cart item updated Successfully!",
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            UserCartProduct.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "Cart item delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cart item not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# --------------------------------------------------------
class UserLoveProductView(viewsets.ViewSet):
    queryset = UserLoveProduct.objects.all()

    def list(self, request):
        user_id = request.query_params.get("user_id")
        if user_id is not None:
            love = UserLoveProduct.objects.filter(user_id=user_id)
        else:
            love = UserLoveProduct.objects.all()
        serializer = UserLoveProductSerializer(instance=love, many=True)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_404_NOT_FOUND,
        )

    def retrieve(self, request, pk=None):
        try:
            love = UserLoveProduct.objects.get(pk=pk)
            serializer = UserLoveProductSerializer(instance=love)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cart item not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def create(self, request):
        data = request.data
        serializer = LoveSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "data": serializer.data,
                "message": "Cart item Created Successfully!",
            },
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            UserLoveProduct.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "User Love product delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "User Love product not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
