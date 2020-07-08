<template>
    <div class="list row">
        <div class="col-md-8">
            <div class="input-group mb-3">
                <input
                        type="text"
                        class="form-control"
                        placeholder="Procurar por nome"
                        v-model="nome"
                />
                <div class="input-group-append">
                    <button
                            class="btn btn-outline-secondary"
                            type="button"
                            @click="searchName"
                    >
                        Procurar
                    </button>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <h4>Lista de Pokémon</h4>
            <ul class="list-group">
                <li
                        class="list-group-item"
                        :class="{ active: index===currentIndex }"
                        v-for="(pokemon, index) in pokemons"
                        :key="index"
                        @click="setActiveName(pokemon, index)"
                >
                    {{ pokemon.name }}
                </li>
            </ul>

            <button class="m-3 btn btn-sm btn-danger" @click="removeAllPokemon">
                Deletar tudo
            </button>
        </div>
        <div class="col-md-6">
            <div v-if="currentPokemon">
                <h4>Pokémon</h4>
                <div>
                    <label><strong>Nome:</strong></label>
                    {{ currentPokemon.name }}
                </div>
                <div>
                    <label><strong>Tamanho:</strong></label>
                    {{ currentPokemon.tamanho }}
                </div>
                <div>
                    <label><strong>Ordem:</strong></label>
                    {{ currentPokemon.ordem }}
                </div>
                <div>
                    <label><strong>Tipo:</strong></label> {{ currentPokemon.tipo.name }} <br>
                    slot: {{ currentPokemon.tipo.slot }} <br>
                    url: {{ currentPokemon.tipo.url }}
                </div>

                <a
                        class="badge badge-warning"
                        :href="'/pokemon/' + currentPokemon.id"
                >
                    Editar
                </a>
            </div>
            <div v-else>
                <br />
                <p>Por favor, clique em um Pokemon...</p>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from "vue-property-decorator";
    import PokemonDataService from "../services/PokemonDataService";

    @Component
    export default class PokemonList extends Vue {
        private pokemons: any[] = [];
        private currentPokemon: any = null;
        private currentIndex: number = -1;
        private nome: string = "";

        retrievePokemon() {
            PokemonDataService.getAll()
                .then((response) => {
                    this.pokemons = response.data;
                    console.log(response.data);
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        refreshList() {
            this.retrievePokemon();
            this.currentPokemon = null;
            this.currentIndex = -1;
        }

        setActiveName(pokemon: any, index: number) {
            this.currentPokemon = pokemon;
            this.currentIndex = index;
            console.log(this.currentPokemon)
            console.log(this.currentPokemon.id)
        }

        removeAllPokemon() {
            PokemonDataService.deleteAll()
                .then((response) => {
                    console.log(response.data);
                    this.refreshList();
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        searchName() {
            PokemonDataService.findByName(this.nome)
                .then((response) => {
                    this.pokemons = response.data;
                    console.log(response.data);
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        mounted() {
            this.retrievePokemon();
        }
    }
</script>

<style scoped>
    .list {
        text-align: left;
        max-width: 750px;
        margin: auto;
    }
</style>