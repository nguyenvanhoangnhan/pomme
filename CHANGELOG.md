#### 2.0.0 (2022-12-15)

##### Chores

*  update seeder ([b824ea43](https://github.com/cyantiz/shoe-shop/commit/b824ea439c4c0249b8888089da9f8ba7a046df95))
*  Update README.md ([0aae3773](https://github.com/cyantiz/shoe-shop/commit/0aae377338fd3b9c7bbdb0891b8e18947a7c1c77))
*  update yarn lock file ([68442d5a](https://github.com/cyantiz/shoe-shop/commit/68442d5a6a445bfba187f4c3291ad20a3e859d9c))
*  update README.md ([be1f671f](https://github.com/cyantiz/shoe-shop/commit/be1f671fd4252d1d9bbb7bcdd53b4c30f3c9f29e))
*  update README.md ([bc2d9b48](https://github.com/cyantiz/shoe-shop/commit/bc2d9b48f27a34153f6077d565b443579dee84b5))
*  update README.md ([1fd8f23d](https://github.com/cyantiz/shoe-shop/commit/1fd8f23d67831c7a100ba23315fa0f578ea1b9db))

##### Continuous Integration

* **web:**
  *  Update web environment variables ([99966e4a](https://github.com/cyantiz/shoe-shop/commit/99966e4a974f112c98bc966c7a1daa3a59427152))
  *  Build with npm instead of yarn ([fd8e2030](https://github.com/cyantiz/shoe-shop/commit/fd8e20305967fd1ca4eecfdd66b2a48802372408))
  *  Add VITE_CLOUDINARY_URL environment variable for web Docker build ([5fec2d95](https://github.com/cyantiz/shoe-shop/commit/5fec2d9589977a78bceba5fc0879c07117e17fb5))
  *  Add environment for web on build ([30692ae1](https://github.com/cyantiz/shoe-shop/commit/30692ae1f9d3b36129397df8af9881434b2ff1c3))
  *  Add environment for web on build ([b2c00282](https://github.com/cyantiz/shoe-shop/commit/b2c002822b381c54ad933f6ed5148973e324a231))
  *  Change expose port for web ([edb5e4dd](https://github.com/cyantiz/shoe-shop/commit/edb5e4dd6219b696ecf4624d2387dcf5222eb0a2))
*  fix typo ([cc01dd99](https://github.com/cyantiz/shoe-shop/commit/cc01dd99d2c3fd212296772808e2b8a5bf4c73f4))
*  Configure vite preview for all hosts, fix machine image cirlce ci ([c4f837b0](https://github.com/cyantiz/shoe-shop/commit/c4f837b0c4e87c876fcf52347e6deb70de9d70d9))
*  Change build tool from npm to yarn ([74957f7e](https://github.com/cyantiz/shoe-shop/commit/74957f7e4e7e7686eb964914151b27092efb8464))
*  Add deploy job to pipeline ([24ced4e2](https://github.com/cyantiz/shoe-shop/commit/24ced4e21caabe87786f9fdc1421dc60454c71aa))
*  Add django plugin for pylint ([#20](https://github.com/cyantiz/shoe-shop/pull/20)) ([a6711a5d](https://github.com/cyantiz/shoe-shop/commit/a6711a5d8c81e60cf9bcafcc2d0c89c885e04d44))
*  setup CircleCI configuration for linting check and building images ([#15](https://github.com/cyantiz/shoe-shop/pull/15)) ([694fd1dd](https://github.com/cyantiz/shoe-shop/commit/694fd1ddbffb70e8fd8188e62d8a322bc445f4d2))
* **api-laravel:**
  *  ignore warning in phpcs ([d922a78a](https://github.com/cyantiz/shoe-shop/commit/d922a78a5daf21bd7ff4163db5bf79567e3823b0))
  *  Add lint test for php code style ([#48](https://github.com/cyantiz/shoe-shop/pull/48)) ([491ee16d](https://github.com/cyantiz/shoe-shop/commit/491ee16d155102e0bbf51b5e50ad63f78b48c24a))
  *  Add CI for Laravel application ([#47](https://github.com/cyantiz/shoe-shop/pull/47)) ([4189d812](https://github.com/cyantiz/shoe-shop/commit/4189d812f0cc25647bbfc9806435ae8e7b2b7faa))

##### New Features

*  implement admin pages ([#59](https://github.com/cyantiz/shoe-shop/pull/59)) ([fd306c3e](https://github.com/cyantiz/shoe-shop/commit/fd306c3e29e7bdacf18d19cafcba7c91fcb7273e))
* update version python package 0.0.3 ([e6be8074](https://github.com/cyantiz/shoe-shop/commit/e6be807490d80d4da3340c006516a06be5cf7c05))
* add python publish package ([a46d130d](https://github.com/cyantiz/shoe-shop/commit/a46d130da0c3f587ed5887716e4b5a0e084ea402))
*  integrate auth api ([44004f0b](https://github.com/cyantiz/shoe-shop/commit/44004f0bd3c77cc9cd764427b47a4b396a641c90))
*  init client code base ([fa973264](https://github.com/cyantiz/shoe-shop/commit/fa9732647b7dc9a04f5ef4430bc1a784a758c23f))
* **web:**
  *  integrate checkout order api ([#56](https://github.com/cyantiz/shoe-shop/pull/56)) ([2a329fdd](https://github.com/cyantiz/shoe-shop/commit/2a329fdd678cd6238d31f0e2f6146892336756ec))
  *  Add moment package and remove redundant package ([4b155ef1](https://github.com/cyantiz/shoe-shop/commit/4b155ef19bafb5fad2398552f44c02f33d5f4e3a))
  *  integrate order detail api ([#55](https://github.com/cyantiz/shoe-shop/pull/55)) ([22f2d268](https://github.com/cyantiz/shoe-shop/commit/22f2d268083bbac2cdcc2b35a8f494614e57a751))
  *  integrate register api and fix cart price ([#54](https://github.com/cyantiz/shoe-shop/pull/54)) ([2d972b6b](https://github.com/cyantiz/shoe-shop/commit/2d972b6b710a8a4aa26a953f79a6f0171d009ee3))
  *  Preview for all hosts in web application ([39d9fe2b](https://github.com/cyantiz/shoe-shop/commit/39d9fe2b477eaa843d4a4cf395f98f88e104cf3e))
  *  Change docker entrypoint and build ([481aabc2](https://github.com/cyantiz/shoe-shop/commit/481aabc2e81f1dd5ea3c2035de5b3d310c7dfe97))
  *  integrate cart api ([#52](https://github.com/cyantiz/shoe-shop/pull/52)) ([e44a2383](https://github.com/cyantiz/shoe-shop/commit/e44a23838f8c904758aa7a799fd873596ef32cf9))
  *  integrate products api ([#51](https://github.com/cyantiz/shoe-shop/pull/51)) ([1568a172](https://github.com/cyantiz/shoe-shop/commit/1568a1726dae01bacf3499abcff3de8a14f8f33c))
  *  integrate api ([#38](https://github.com/cyantiz/shoe-shop/pull/38)) ([0040a143](https://github.com/cyantiz/shoe-shop/commit/0040a143fabb0978bb95894e20287668e677a21d))
  *  add client filter logic ([#35](https://github.com/cyantiz/shoe-shop/pull/35)) ([5feb4c2b](https://github.com/cyantiz/shoe-shop/commit/5feb4c2bd9a20e02f8352571c2f3741fa79f625f))
  *  add product detail page UI ([#32](https://github.com/cyantiz/shoe-shop/pull/32)) ([a3cb13ac](https://github.com/cyantiz/shoe-shop/commit/a3cb13acd7959619375e05e44ee0a1e1154b018c))
  *  add product list page UI ([#29](https://github.com/cyantiz/shoe-shop/pull/29)) ([902d3a6f](https://github.com/cyantiz/shoe-shop/commit/902d3a6fa6dfee292793dd85786eba8ebc8addb1))
  *  add axios instance ([#26](https://github.com/cyantiz/shoe-shop/pull/26)) ([3aa5a9d0](https://github.com/cyantiz/shoe-shop/commit/3aa5a9d0ad11dfe919ab0324b95853285c4ebab2))
  *  add order page UI ([#21](https://github.com/cyantiz/shoe-shop/pull/21)) ([1e7a4ada](https://github.com/cyantiz/shoe-shop/commit/1e7a4ada36ad545a7a2f8c1338099c17843b70a7))
  *  add cart page UI ([#14](https://github.com/cyantiz/shoe-shop/pull/14)) ([c8949970](https://github.com/cyantiz/shoe-shop/commit/c8949970b310fccc4c1221014eb72c6358d46268))
  *  dockerize vuejs application ([#12](https://github.com/cyantiz/shoe-shop/pull/12)) ([d5790a06](https://github.com/cyantiz/shoe-shop/commit/d5790a06f47828da83502386ad036a229fc06d88))
  *  add reset password page ([#5](https://github.com/cyantiz/shoe-shop/pull/5)) ([96aae1ea](https://github.com/cyantiz/shoe-shop/commit/96aae1eac0e72b1a4aa84dd83e5c181947f0d122))
  *  add sidecart and footer ([#4](https://github.com/cyantiz/shoe-shop/pull/4)) ([f334b35a](https://github.com/cyantiz/shoe-shop/commit/f334b35a0d40bbf994087852069bc37118685b47))
  *  add 404 page ([#2](https://github.com/cyantiz/shoe-shop/pull/2)) ([4492beb1](https://github.com/cyantiz/shoe-shop/commit/4492beb1fec4c18564f97add2689a8c5f4441f5f))
  *  add auth pages ([#3](https://github.com/cyantiz/shoe-shop/pull/3)) ([0015b399](https://github.com/cyantiz/shoe-shop/commit/0015b39961c589c38f8eaab1b1ed3709989f7042))
  *  add header ([#1](https://github.com/cyantiz/shoe-shop/pull/1)) ([fab49c6d](https://github.com/cyantiz/shoe-shop/commit/fab49c6db29c916206bc56cff973a044098a49b9))
* **api-laravel:**
  *  Change log time to json ([dc0cc8b2](https://github.com/cyantiz/shoe-shop/commit/dc0cc8b2e3c18f909127664df8cf7d506c3e1b9c))
  *  Add log for all requests ([696d315f](https://github.com/cyantiz/shoe-shop/commit/696d315f9f1a530d4be7908068abbb73608ec173))
  *  Add log for all requests ([f1a9439b](https://github.com/cyantiz/shoe-shop/commit/f1a9439b74369bed9c621edf028bf0bf24f3f88b))
  *  Dockerise laravel application, modify example env values ([#46](https://github.com/cyantiz/shoe-shop/pull/46)) ([b9fe4c86](https://github.com/cyantiz/shoe-shop/commit/b9fe4c86bca5ae459748008e20a1631f3f860152))
* **api:**
  *  Add and configure logging middleware ([c7bfd698](https://github.com/cyantiz/shoe-shop/commit/c7bfd698ce65426d1e74f2a37a4672ae14ab741f))
  *  add jwt ([#43](https://github.com/cyantiz/shoe-shop/pull/43)) ([87fc89c4](https://github.com/cyantiz/shoe-shop/commit/87fc89c4174c509de6b5d9c6920263f450dddba1))
  * add env.example ([#33](https://github.com/cyantiz/shoe-shop/pull/33)) ([1db8bdd0](https://github.com/cyantiz/shoe-shop/commit/1db8bdd0d53df4bed340d58fed36b5637d3d397a))
  * add api for shoes, accessory, cloth ([#27](https://github.com/cyantiz/shoe-shop/pull/27)) ([b6656f5a](https://github.com/cyantiz/shoe-shop/commit/b6656f5a25751348047a63ca0c95922c54e44166))
  *  dockerize django application, change allowed hosts to * ([fdab22eb](https://github.com/cyantiz/shoe-shop/commit/fdab22eb6b9c20373f67304f6080d7d60be90450))
  *  add CRUD for shoe model ([#10](https://github.com/cyantiz/shoe-shop/pull/10)) ([0a105d98](https://github.com/cyantiz/shoe-shop/commit/0a105d983e5b321bf77bd2ed31cec4c15890d6df))
  *  create model in DRF ([#6](https://github.com/cyantiz/shoe-shop/pull/6)) ([119f9e06](https://github.com/cyantiz/shoe-shop/commit/119f9e06ff0f8fc282e424c6769eeab9c6c329d0))
* **api_laravel:**
  *  add sentry/sentry-laravel ([a5e05f50](https://github.com/cyantiz/shoe-shop/commit/a5e05f5071e55847e49c8810ef95d987317e38c7))
  *  implement basic api ([#44](https://github.com/cyantiz/shoe-shop/pull/44)) ([76a1ef6a](https://github.com/cyantiz/shoe-shop/commit/76a1ef6a7f1f60c69373829d92639b35051e2cd0))
* **db:**  provision postgres DB with docker, compose, modify README for instruction ([#13](https://github.com/cyantiz/shoe-shop/pull/13)) ([a21d1977](https://github.com/cyantiz/shoe-shop/commit/a21d197773316fe04d20799f8a0e6fcdd507d2ef))

##### Bug Fixes

* **api_laravel:**
  *  fix build failed caused by syntax ([fe7aecd3](https://github.com/cyantiz/shoe-shop/commit/fe7aecd3faeef92122630bc8c367bb7c4fab082a))
  *  fix \'Closure route handler is forbidden\' ([#49](https://github.com/cyantiz/shoe-shop/pull/49)) ([630937a5](https://github.com/cyantiz/shoe-shop/commit/630937a548cfabc6580ed2970afd42852c42ddf9))
  *  fix validator error ([#45](https://github.com/cyantiz/shoe-shop/pull/45)) ([4260ea18](https://github.com/cyantiz/shoe-shop/commit/4260ea1808c8b5a975e19612972fd2767f4a8109))
* **web:**
  *  fix redirect to login page from products page ([1b208020](https://github.com/cyantiz/shoe-shop/commit/1b2080208b4cad5cb6d9f425439e5238f51eb34a))
  *  fix auto redirect to login page when user havent logged in ([#61](https://github.com/cyantiz/shoe-shop/pull/61)) ([b48df364](https://github.com/cyantiz/shoe-shop/commit/b48df364e23c0cebdf63dc1979a9a769914cd9cb))
  *  fix ts errors ([#53](https://github.com/cyantiz/shoe-shop/pull/53)) ([5a11c7b8](https://github.com/cyantiz/shoe-shop/commit/5a11c7b88e61633b281e7be8c554fa0a3f9c82f4))
* **api-laravel:**
  *  fix lint in log message ([396e85a2](https://github.com/cyantiz/shoe-shop/commit/396e85a2c8d92783732dca92681bc724e137974c))
  *  fix lint for camelCase ([0a80d9b1](https://github.com/cyantiz/shoe-shop/commit/0a80d9b19ea6078ea8b84378d3fc48d4f2ba11b8))
*  fix lint ([6282f050](https://github.com/cyantiz/shoe-shop/commit/6282f0507ff2c5fa91c066cc16d5bf5972eb0988))
*  changing env file ([b976097a](https://github.com/cyantiz/shoe-shop/commit/b976097aec40b35dd07ba36d3048d42cb3aee700))
*  remove generating key command ([7c35a8e0](https://github.com/cyantiz/shoe-shop/commit/7c35a8e09309c76b5e60c659635c1f64a1e4dcce))
*  remove DB migration from Dockerfile ([14943388](https://github.com/cyantiz/shoe-shop/commit/1494338806107824e6bacba60e13246044c39da1))
*  fix location of API docker build ([46241b47](https://github.com/cyantiz/shoe-shop/commit/46241b47fa5029f611946fe28fee385ecbdd71ef))
* **ci-laravel:**  fix typo ([34bf9062](https://github.com/cyantiz/shoe-shop/commit/34bf9062dae1e49e64fd3f77bf2e95a289127df8))
* **api:**
  *  Remove sensitive data, refactor env file ([#36](https://github.com/cyantiz/shoe-shop/pull/36)) ([e9b44ea2](https://github.com/cyantiz/shoe-shop/commit/e9b44ea27683547a7235dae70fbb2b6aea743b49))
  *  fix register ([4069c17f](https://github.com/cyantiz/shoe-shop/commit/4069c17f3bbbe8b17c7a78a0703ff6dbfe2411f3))
  *  fix api product ([#31](https://github.com/cyantiz/shoe-shop/pull/31)) ([6293b937](https://github.com/cyantiz/shoe-shop/commit/6293b937c2e31671556872a30fa5332dbe53eb54))
  * fix CRUD of shoes ([862bd16c](https://github.com/cyantiz/shoe-shop/commit/862bd16cab0971ecce2a8705b22fefee5d19cd14))
* **database:**
  *  fix model OrderProduct ([#16](https://github.com/cyantiz/shoe-shop/pull/16)) ([0cf819a5](https://github.com/cyantiz/shoe-shop/commit/0cf819a5922c3aef1224a1da1534f753779ce855))
  *  fix model OrderProduct ([27021998](https://github.com/cyantiz/shoe-shop/commit/27021998348de97ff46f971e94b81b5485d34296))

##### Other Changes

*  Add deploying, logging, Nginx configurations ([#58](https://github.com/cyantiz/shoe-shop/pull/58)) ([7641f50d](https://github.com/cyantiz/shoe-shop/commit/7641f50dd6f16974e1b771007e4301e6e29119e6))
* cyantiz/shoe-shop into develop ([63271c67](https://github.com/cyantiz/shoe-shop/commit/63271c67b8b546fda181a3c2831118b8ba24596f))
* cyantiz/shoe-shop into develop ([a862a566](https://github.com/cyantiz/shoe-shop/commit/a862a5662c9e9bbaa754efb0619da0ea4cc23ec4))
* //github.com/cyantiz/shoe-shop into develop ([493349b1](https://github.com/cyantiz/shoe-shop/commit/493349b1e8cb7303938d3b65cc2be09ea6f67acb))
* cyantiz/shoe-shop into develop ([a45a4674](https://github.com/cyantiz/shoe-shop/commit/a45a467498a7c9700e664eda98bc85b29026450d))
*  Add PR template and contributing guideline ([#17](https://github.com/cyantiz/shoe-shop/pull/17)) ([8397a725](https://github.com/cyantiz/shoe-shop/commit/8397a72548a97af0148822420df92ad426c5493d))
*  Change env DB URL in README.md ([e4df2c73](https://github.com/cyantiz/shoe-shop/commit/e4df2c735aa3eb1877ab6397c962d29c303872db))
* **api:**
  *  crud user-cart-product and user-love-product ([#25](https://github.com/cyantiz/shoe-shop/pull/25)) ([d19f18c9](https://github.com/cyantiz/shoe-shop/commit/d19f18c9169f667e3533650d03938e41807cf2cb))
  *  Add sentry configuration ([#22](https://github.com/cyantiz/shoe-shop/pull/22)) ([eb949ec3](https://github.com/cyantiz/shoe-shop/commit/eb949ec3e44dd68281b6dac2cbcf8cfc79c374e4))

##### Refactors

*  remove .vscode directory ([422ab1b5](https://github.com/cyantiz/shoe-shop/commit/422ab1b5a2c688d313787da4e5bc6c3092e17421))

##### Code Style Changes

* **api_laravel:**  add phpcs and phpcbf along with SunAsteriskLaravel ruleset ([#41](https://github.com/cyantiz/shoe-shop/pull/41)) ([6ea9d386](https://github.com/cyantiz/shoe-shop/commit/6ea9d3869f9652a16783e7a7ebf03981cb329faa))
*  Modify readme and remove redundant .env.example ([#37](https://github.com/cyantiz/shoe-shop/pull/37)) ([ce9f6c14](https://github.com/cyantiz/shoe-shop/commit/ce9f6c148b24727c893f0b978393b545f66aa65f))

