interface Product {
    id: number
    name: string
    price: number
    thumbnailUrl: string
}

interface CartItem extends Product {
    quantity: number
}
