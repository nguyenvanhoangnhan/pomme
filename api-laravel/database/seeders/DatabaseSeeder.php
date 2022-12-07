<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Carbon;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // \App\Models\User::factory(10)->create();

        $users = [
            ['nhan053qt@gmail.com', 'Admin', 'pwd123', 'admin'],
            ['nguyen.vh.nhan@gmail.com', 'Nguyễn Văn Hoàng Nhân', 'pwd123', 'customer'],
            ['letronghoangminh@gmail.com', 'Lê Trọng Hoàng Minh', 'pwd123', 'customer'],
        ];

        $shoes = [
            // [name, price, discount%, in_stock, sold, gender, series, shape]
            ['GSmith #1', 500000, 0, 100, 0, 2, 'GSmith', 0],
            ['GSmith #2', 600000, 0, 100, 0, 2, 'GSmith', 0],
            ['GSmith #3', 700000, 0, 100, 0, 2, 'GSmith', 1],
            ['GSmith #6', 800000, 0, 100, 0, 2, 'GSmith', 0],
            ['Crispin #1', 900000, 0, 100, 0, 2, 'Crispin', 0],
            ['Crispin #2', 990000, 0, 100, 0, 2, 'Crispin', 1],
            ['Crispin #3', 999000, 10, 100, 0, 1, 'Crispin', 0],
            ['Crispin #4', 800000, 0, 100, 0, 2, 'Crispin', 1],
            ['Shizuka #1', 1111111, 0, 100, 0, 0, 'Shizuka', 0],
            ['Shizuka #2', 800000, 0, 100, 0, 1, 'Shizuka', 1],
            ['Shizuka #3', 999000, 0, 100, 0, 2, 'Shizuka', 0],
            ['Shizuka #4', 800000, 0, 100, 0, 2, 'Shizuka', 1],
            ['Rhode #1', 800000, 0, 100, 0, 2, 'Rhode', 1],
            ['Rhode #2', 300000, 0, 100, 0, 2, 'Rhode', 0],
            ['Rhode #3', 800000, 0, 100, 0, 2, 'Rhode', 1],
            ['Rhode #4', 999000, 0, 100, 0, 1, 'Rhode', 0],
            ['Rhode #5', 800000, 0, 100, 0, 1, 'Rhode', 1],
            ['Rhode #6', 500000, 0, 100, 0, 0, 'Rhode', 0],
        ];

        $accessories = [
            // [name, price, discount_percent, in_stock, sold, category]
            ['Shock #1', 100000, 0, 100, 0, 'Shock'],
            ['Shock #2', 200000, 0, 100, 0, 'Shock'],
            ['Shock #3', 300000, 0, 100, 0, 'Shock'],
            ['Shock #4', 400000, 0, 100, 0, 'Shock'],
            ['Shock #5', 500000, 0, 100, 0, 'Shock'],
            ['Shock #6', 600000, 0, 100, 0, 'Shock'],
            ['Shock #7', 700000, 0, 100, 0, 'Shock'],
            ['Shock #8', 800000, 0, 100, 0, 'Shock'],
            ['Tote #1', 100000, 0, 100, 0, 'Tote'],
            ['Tote #2', 200000, 0, 100, 0, 'Tote'],
            ['Tote #3', 300000, 0, 100, 0, 'Tote'],
            ['Tote #4', 400000, 0, 100, 0, 'Tote'],
            ['Tote #5', 500000, 0, 100, 0, 'Tote'],
            ['Tote #6', 600000, 0, 100, 0, 'Tote'],
            ['Tote #7', 700000, 0, 100, 0, 'Tote'],
            ['Tote #8', 800000, 0, 100, 0, 'Tote'],
            ['Tote #9', 900000, 0, 100, 0, 'Tote'],
            ['Shoelace #1', 100000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #2', 200000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #3', 300000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #4', 400000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #5', 500000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #6', 600000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #7', 700000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #8', 800000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #9', 900000, 0, 100, 0, 'Shoelace'],
            ['Shoelace #10', 100000, 0, 100, 0, 'Shoelace'],
            ['Backpack #1', 100000, 0, 100, 0, 'Backpack'],
            ['Backpack #2', 200000, 0, 100, 0, 'Backpack'],
            ['Backpack #3', 300000, 0, 100, 0, 'Backpack'],
            ['Backpack #4', 400000, 0, 100, 0, 'Backpack'],
            ['Backpack #5', 500000, 0, 100, 0, 'Backpack'],
            ['Backpack #6', 600000, 0, 100, 0, 'Backpack'],
            ['Backpack #7', 700000, 0, 100, 0, 'Backpack'],
            ['Backpack #8', 800000, 0, 100, 0, 'Backpack'],
            ['Backpack #9', 900000, 0, 100, 0, 'Backpack'],
            ['Backpack #10', 100000, 0, 100, 0, 'Backpack'],
        ];

        $clothes = [
            ['Tee #1', 100000, 0, 100, 0, 'Tee'],
            ['Tee #2', 200000, 0, 100, 0, 'Tee'],
            ['Tee #3', 300000, 0, 100, 0, 'Tee'],
            ['Tee #4', 400000, 0, 100, 0, 'Tee'],
            ['Tee #5', 500000, 0, 100, 0, 'Tee'],
            ['Tee #6', 600000, 0, 100, 0, 'Tee'],
            ['Tee #7', 700000, 0, 100, 0, 'Tee'],
            ['Tee #8', 800000, 0, 100, 0, 'Tee'],
            ['Hoodie #1', 100000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #2', 200000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #3', 300000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #4', 400000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #5', 500000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #6', 600000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #7', 700000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #8', 800000, 0, 100, 0, 'Hoodie'],
            ['Hoodie #9', 900000, 0, 100, 0, 'Hoodie'],
            ['Sweatshirt #1', 100000, 0, 100, 0, 'Sweatshirt'],
            ['Sweatshirt #2', 200000, 0, 100, 0, 'Sweatshirt'],
            ['Sweatshirt #3', 300000, 0, 100, 0, 'Sweatshirt'],
            ['Sweatshirt #4', 400000, 0, 100, 0, 'Sweatshirt'],
        ];

        foreach ($users as $user) {
            \App\Models\User::create([
                'email' => $user[0],
                'name' => $user[1],
                'password' => bcrypt($user[2]),
                'role' => $user[3],
            ]);
        }

        foreach ($shoes as $shoe) {
            $product = \App\Models\Product::create([
                'name' => $shoe[0],
                'price' => $shoe[1],
                'discount_percent' => $shoe[2],
                'in_stock' => $shoe[3],
                'sold' => $shoe[4],
                'type' => 'shoe',
            ]);

            \App\Models\Shoe::create([
                'product_id' => $product->id,
                'gender' => $shoe[5],
                'series' => $shoe[6],
                'shape' => $shoe[7],
            ]);
        }

        // seed shoe children (sizes)
        foreach (\App\Models\Shoe::all() as $shoe) {
            for ($size = 35; $size <= 46; $size++) {
                \App\Models\ShoeChild::create([
                    'shoe_id' => $shoe->id,
                    'size' => $size,
                    'in_stock' => 100,
                ]);
            }
        }

        foreach ($accessories as $accessory) {
            $product = \App\Models\Product::create([
                'name' => $accessory[0],
                'price' => $accessory[1],
                'discount_percent' => $accessory[2],
                'in_stock' => $accessory[3],
                'sold' => $accessory[4],
                'type' => 'accessory',
            ]);

            \App\Models\Accessory::create([
                'product_id' => $product->id,
                'category' => $accessory[5],
            ]);
        }

        foreach ($clothes as $cloth) {
            $product = \App\Models\Product::create([
                'name' => $cloth[0],
                'price' => $cloth[1],
                'discount_percent' => $cloth[2],
                'in_stock' => $cloth[3],
                'sold' => $cloth[4],
                'type' => 'clothes',
            ]);

            \App\Models\Clothes::create([
                'product_id' => $product->id,
                'category' => $cloth[5],
            ]);
        }

        // seed product images
        foreach (\App\Models\Product::all() as $product) {
            \App\Models\Image::create([
                'is_thumbnail' => true,
                'url' => 'https://via.placeholder.com/500/8b8b8b/ffffff?text=Thumbnail',
                'product_id' => $product->id,
            ]);
            \App\Models\Image::create([
                'url' => 'https://via.placeholder.com/500/8b8b8b/ffffff?text=Image+1',
                'product_id' => $product->id,
            ]);
            \App\Models\Image::create([
                'url' => 'https://via.placeholder.com/500/35495/ffffff?text=Image+2',
                'product_id' => $product->id,
            ]);
            \App\Models\Image::create([
                'url' => 'https://via.placeholder.com/500/8b8b8b/ffffff?text=Image+3',
                'product_id' => $product->id,
            ]);
            \App\Models\Image::create([
                'url' => 'https://via.placeholder.com/500/35495/ffffff?text=Image+4',
                'product_id' => $product->id,
            ]);
        }

        // seed product cart items of user 1
        // pick 5 random products
        $cartProducts = \App\Models\Product::inRandomOrder()->limit(5)->get();
        foreach ($cartProducts as $product) {
            \App\Models\UserCartProduct::create([
                'user_id' => 2,
                'product_id' => $product->id,
                'quantity' => rand(1, 5),
                'size' => $product->type === 'shoe' ? rand(35, 46) : null,
            ]);
        }

        // seed order for user 1
        $orderProducts = \App\Models\Product::inRandomOrder()->limit(5)->get();
        $orderQuantities = [1, 2, 3, 4, 5];
        // totalPrice = sum of (product price * quantity)
        $totalPrice = 0;
        foreach ($orderProducts as $index => $product) {
            $totalPrice += $product->price * $orderQuantities[$index];
        }

        // orderName is string contain product names, separated by comma
        $orderName = $orderProducts->pluck('name')->implode(', ');

        $deliveryFee = 30000;

        $order = \App\Models\Order::create([
            'user_id' => 2,
            'name' => $orderName,
            'receiver_name' => 'Nguyễn Văn Hoàng Nhân',
            'status' => 'shipping',
            'shipping_at' => Carbon::now()->addDays(3),
            'total_price' => $totalPrice,
            'delivery_fee' => $deliveryFee,
            'address' => '54 Nguyễn Lương Bằng',
            'province_code' => '48',
            'district_code' => '490',
            'commune_code' => '20197',
            'phone' => '0123456789',
        ]);
        foreach ($orderProducts as $index => $product) {
            \App\Models\OrderProduct::create([
                'order_id' => $order->id,
                'product_id' => $product->id,
                'quantity' => $orderQuantities[$index],
                'price_at_order' => $product->price,
                'size' => $product->type === 'shoe' ? rand(35, 46) : null,
            ]);
        }

        // seed product wishlist items of user 1
        // pick 5 random products
        $wishlistProducts = \App\Models\Product::inRandomOrder()->limit(5)->get();
        foreach ($wishlistProducts as $product) {
            \App\Models\UserLoveProduct::create([
                'user_id' => 2,
                'product_id' => $product->id,
            ]);
        }
    }
}
