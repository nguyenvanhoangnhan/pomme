interface Image {
    image_id: number
    product_id: number
    is_thumbnail: boolean
    url: string
}

interface Product {
    product_id: number
    name: string
    price: number
    sale_percent: number
    in_stock: number
    images: Image[]
    type: 1 | 2 | 3
    // 1: shoe | 2: accessory | 3: clothes
}

interface Shoe {
    shoe_id: number
    product_id: number
    gender: 0 | 1 | 2
    series: String
    shape: 0 | 1
    product: Product
}

interface CartItem extends Product {
    quantity: number
}

interface OrderProduct {
    order_product_id: number
    order_id: number
    product_id: number
    price_at_order: number
    quantity: number
    product: Product
    size: number | null
}

interface Order {
    order_id: number
    user_id: number
    address: string
    province_id: number
    district_id: number
    commune_id: number
    status: 0 | 1 | 2
    // 0 = in progress, 1 = shipping, 2 = delivered
    total: number
    discount: number
    created_at: string
    shipping_at: string
    delivered_at: string
    products: OrderProduct[]
}
