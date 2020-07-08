import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
    {
        path: "/",
        alias: "/pokemons",
        name: "pokemons",
        // @ts-ignore
        component: () => import('../components/PoquemonList.vue')
    },
    {
        path: "/pokemon/:id",
        name: "pokemon",
        // @ts-ignore
        component: () => import("../components/Pokemon.vue")
    },
    {
        path: "/add",
        name: "add",
        // @ts-ignore
        component: () => import("../components/CreatePokemon.vue")
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;