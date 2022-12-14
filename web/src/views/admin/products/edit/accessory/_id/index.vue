<script setup lang="ts">
import api from "@/api"
import router from "@/router"
import { Modal, notification } from "ant-design-vue"
import axios from "axios"
import { onMounted, reactive, ref } from "vue"
import { useRoute } from "vue-router"

defineProps<{}>()

interface AccessoryEditFormState {
    id: number
    product_id: number
    name: string
    price: number
    in_stock: number
    discount_percent: number
    sold: number
    thumbnail: any
    images: any[]
    type: "accessory"
    category: string
}

const route = useRoute()
const id = Number(route.params.id)
const isInitialLoading = ref<boolean>(true)
const isHandling = ref<boolean>(false)
const formState = reactive<AccessoryEditFormState>({
    id: 0,
    product_id: 0,
    name: "",
    price: 0,
    discount_percent: 0,
    in_stock: 0,
    sold: 0,
    thumbnail: null,
    images: [],
    type: "accessory",
    category: "",
})

const onOk = async () => {
    isHandling.value = true
    try {
        const images = formState.images.map((img) => img.url)
        const thumbnail = formState.thumbnail.url

        const data = {
            accessory_id: formState.id,
            name: formState.name,
            price: formState.price,
            in_stock: formState.in_stock,
            discount_percent: formState.discount_percent,
            thumbnail,
            images,
            category: formState.category,
        }

        await api.put(`/products/accessories`, data).then(() => {
            router.push({ name: "Product Management - List" })
        })
        router.push({ name: "Product Management - List" })
        Modal.success({
            title: "Success",
            content: "Product updated successfully",
        })
    } catch (err: any) {
        console.log(err)
        notification.error({
            message: "Error",
            description: err.message || "Something went wrong",
        })
    } finally {
        isHandling.value = false
    }
}

const onCancel = () => {
    router.push({ name: "Product Management - List" })
}

onMounted(async () => {
    isInitialLoading.value = true
    const res = await api.get(`/products/accessories/${id}`)
    const shoe = res.data as ClothesWithProduct
    isInitialLoading.value = false

    //
    formState.id = shoe.id
    formState.product_id = shoe.product_id
    formState.name = shoe.product.name
    formState.price = shoe.product.price
    formState.discount_percent = shoe.product.discount_percent
    formState.in_stock = shoe.product.in_stock
    formState.sold = shoe.product.sold

    //
    const thumbnailUrl = shoe.product.images.find((img) => img.is_thumbnail)?.url
    if (thumbnailUrl) {
        // convert to antd upload file
        formState.thumbnail = {
            uid: "thumbnail",
            name: "thumbnail",
            status: "done",
            url: thumbnailUrl,
        }
    }

    const imagesUrls = shoe.product.images.filter((img) => !img.is_thumbnail).map((img) => img.url)
    if (imagesUrls.length > 0) {
        // convert to antd upload file
        formState.images = imagesUrls.map((url) => ({
            uid: url,
            name: url,
            status: "done",
            url,
        }))
    }

    formState.category = shoe.category
})

const uploadToCloudinary = async (file: File) => {
    try {
        isHandling.value = true
        const formData = new FormData()
        const cloudName: string = import.meta.env.VITE_CLOUDINARY_NAME
        const preset: string = import.meta.env.VITE_CLOUDINARY_PRESET
        formData.append("file", file)
        formData.append("upload_preset", preset)
        const res = await axios.post(`https://api.cloudinary.com/v1_1/${cloudName}/image/upload`, formData)
        const data = res.data
        isHandling.value = false
        return data.url
    } catch (err: any) {
        console.log(err)
        notification.error({
            message: "Error",
            description: err.message || "Something went wrong",
        })
        isHandling.value = false
        return "https://via.placeholder.com/500/dddddd/34495e?text=Image"
    }
}

const beforeUploadThumbnail = async (file: File) => {
    formState.thumbnail = {
        uid: "thumbnail",
        name: "thumbnail",
        status: "uploading",
        url: URL.createObjectURL(file),
    }
    const url = await uploadToCloudinary(file)
    formState.thumbnail = {
        uid: "thumbnail",
        name: "thumbnail",
        status: "done",
        url,
    }
}

const onRemoveThumbnail = () => {
    const defaultThumbnailUrl = "https://via.placeholder.com/500/dddddd/34495e?text=Thumbnail"
    formState.thumbnail = {
        uid: "thumbnail",
        name: "thumbnail",
        status: "done",
        url: defaultThumbnailUrl,
    }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const onThumbnailChange = (info: any) => {
    if (info.file.status === "done") {
        formState.thumbnail = info.file.originFileObj
    }
}

const beforeUploadImages = async (file: File) => {
    // push a temp file to images
    const uid = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15)
    formState.images.push({
        uid,
        name: file.name,
        status: "uploading",
        url: URL.createObjectURL(file),
    })
    const url = await uploadToCloudinary(file)
    formState.images.pop()
    formState.images.push({
        uid: url,
        name: url,
        status: "done",
        url,
    })
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const onRemoveImages = (file: any) => {
    formState.images = formState.images.filter((img) => img.uid !== file.uid)
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const onImagesChange = (info: any) => {
    if (info.file.status === "done") {
        formState.images.push(info.file.originFileObj)
    }
}

const CATEGORIES = ["Shock", "Shoelace", "Tote", "Backpack"]
</script>

<template>
    <a-modal :visible="$route.name === 'Product Management - Edit Accessory'" title="Chỉnh sửa sản phẩm" ok-text="Sửa" cancel-text="Hủy" @ok="onOk" width="800px" @cancel="onCancel">
        <div v-if="isInitialLoading" class="form-skeleton">
            <a-skeleton :paragraph="{ rows: 12 }" active></a-skeleton>
        </div>
        <a-form v-else ref="formRef" :model="formState" layout="horizontal" :label-col="{ span: 6 }" label-align="right" name="form_in_modal" class="relative">
            <div class="saving absolute w-full h-full flex justify-center items-center z-[999]" v-show="isHandling">
                <a-spin></a-spin>
            </div>
            <div style="max-height: 480px; overflow-y: scroll; padding-inline: 1rem">
                <a-form-item name="product_id" label="Mã SP" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-input v-model:value="formState.product_id" disabled />
                </a-form-item>
                <a-form-item name="name" label="Tên" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-input v-model:value="formState.name" />
                </a-form-item>
                <a-form-item name="price" label="Giá" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-input-number
                        v-model:value="formState.price"
                        style="width: 160px"
                        addon-before="₫"
                        :formatter="(value: string) => `${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
                    ></a-input-number>
                </a-form-item>
                <a-form-item name="discount_percent" label="Giảm giá (%)" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-input-number v-model:value="formState.discount_percent" style="width: 160px" addon-before="+" :min="0" :max="100" :precision="0"></a-input-number>
                </a-form-item>
                <a-form-item name="in_stock" label="Trong kho" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-input-number v-model:value="formState.in_stock" style="width: 160px" addon-before="+" :min="0" :precision="0"></a-input-number>
                </a-form-item>
                <a-form-item name="sold" label="Đã bán" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-input-number v-model:value="formState.sold" style="width: 160px" addon-before="+" disabled></a-input-number>
                </a-form-item>
                <a-form-item name="category" label="Loại" :rules="[{ required: true, message: 'Bạn chưa chọn trường này!' }]">
                    <a-select v-model:value="formState.category">
                        <a-select-option v-for="category in CATEGORIES" :key="category" :value="category">{{ category }}</a-select-option>
                    </a-select>
                </a-form-item>

                <!-- upload thumbnail -->
                <a-form-item name="thumbnail" label="Ảnh đại diện" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-upload
                        :file-list="formState.thumbnail ? [formState.thumbnail] : []"
                        :before-upload="beforeUploadThumbnail"
                        :on-remove="onRemoveThumbnail"
                        :on-change="onThumbnailChange"
                        :multiple="false"
                        :show-upload-list="true"
                        list-type="picture-card"
                        accept="image/*"
                    >
                        Chọn ảnh
                    </a-upload>
                </a-form-item>

                <!-- upload images -->
                <a-form-item name="images" label="Ảnh chi tiết" :rules="[{ required: true, message: 'Bạn chưa nhập trường này!' }]">
                    <a-upload
                        :file-list="formState.images"
                        :before-upload="beforeUploadImages"
                        :on-remove="onRemoveImages"
                        :on-change="onImagesChange"
                        :multiple="true"
                        :show-upload-list="true"
                        list-type="picture-card"
                        accept="image/*"
                    >
                        Chọn ảnh
                    </a-upload>
                </a-form-item>
            </div>
        </a-form>
    </a-modal>
</template>

<style lang="less" scoped></style>
