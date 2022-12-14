import { useLoadingStore } from "./loading"
import { defineStore } from "pinia"
import api from "@/api"
import { notification } from "ant-design-vue"

interface AreaStoreDistricts {
    province_code: string
    list: AreaDistrict[]
}

interface AreaStoreCommunes {
    district_code: string
    list: AreaCommune[]
}

export const useAreaStore = defineStore("area", {
    state: () => ({
        provinces: [] as AreaProvince[],
        districts: [] as AreaStoreDistricts[],
        communes: [] as AreaStoreCommunes[],
    }),
    actions: {
        async fetchProvinces() {
            if (this.provinces.length) return
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.get("https://api.mysupership.vn/v1/partner/areas/province")
                this.provinces = data.results
                this.updateLocalStorage()
            } catch (error: any) {
                notification.error({
                    message: "Lỗi",
                    description: error.message || "Có lỗi xảy ra, vui lòng thử lại sau",
                })
            }
            useLoadingStore().loadingOff()
        },
        async fetchDistricts(code: string) {
            if (this.districts.find((item) => item.province_code === code)) return
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.get(`https://api.mysupership.vn/v1/partner/areas/district?province=${code}`)
                const districts = {
                    province_code: code,
                    list: data.results,
                }
                this.districts.push(districts)
                this.updateLocalStorage()
            } catch (error: any) {
                notification.error({
                    message: "Lỗi",
                    description: error.message || "Có lỗi xảy ra, vui lòng thử lại sau",
                })
            }
            useLoadingStore().loadingOff()
        },
        async fetchCommunes(code: string) {
            if (this.communes.find((item) => item.district_code === code)) return
            useLoadingStore().loadingOn()
            try {
                const { data } = await api.get(`https://api.mysupership.vn/v1/partner/areas/commune?district=${code}`)
                const communes = {
                    district_code: code,
                    list: data.results,
                }
                this.communes.push(communes)
            } catch (error: any) {
                notification.error({
                    message: "Lỗi",
                    description: error.message || "Có lỗi xảy ra, vui lòng thử lại sau",
                })
            }
            useLoadingStore().loadingOff()
        },
        loadFromLocalStorage() {
            const provinces = localStorage.getItem("provinces")
            const districts = localStorage.getItem("districts")
            const communes = localStorage.getItem("communes")
            if (provinces) this.provinces = JSON.parse(provinces)
            if (districts) this.districts = JSON.parse(districts)
            if (communes) this.communes = JSON.parse(communes)
        },
        updateLocalStorage() {
            localStorage.setItem("provinces", JSON.stringify(this.provinces))
            localStorage.setItem("districts", JSON.stringify(this.districts))
            localStorage.setItem("communes", JSON.stringify(this.communes))
        },
    },
})
