<template>
    <div v-if="currentPokemon" class="edit-form">
        <h4>Pokemon</h4>
        <form>
            <div class="form-group">
                <label for="nome">Nome</label>
                <input
                        type="text"
                        class="form-control"
                        id="nome"
                        v-model="currentPokemon.name"
                />
            </div>
            <div class="form-group">
                <label for="tamanho">Tamanho</label>
                <input
                        type="text"
                        class="form-control"
                        id="tamanho"
                        v-model="currentPokemon.tamanho"
                />
            </div>
            <div class="form-group">
                <label for="ordem">Ordem</label>
                <input
                        class="form-control"
                        id="ordem"
                        v-model="currentPokemon.ordem"
                />
            </div>
            <div class="form-group">
                <label for="tipo">Tipo</label>
                <select
                        class="form-control"
                        id="tipo"
                        v-model="currentPokemon.selected"
                >
                    <option v-for="tipo in currentPokemon.tipo" v-bind:value="tipo">
                        {{ tipo.name }}
                    </option>
                </select>
            </div>
        </form>

        <button class="badge badge-danger mr-2" @click="deletePokemon">
            Excluir
        </button>

        <button type="submit" class="badge badge-success" @click="updatePokemon">
            Atualizar
        </button>
        <p>{{ message }}</p>
    </div>

    <div v-else>
        <br />
        <p>Por favor, clique em um Pokemon...</p>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from "vue-property-decorator";
    import PokemonDataService from "../services/PokemonDataService";

    @Component
    export default class Pokemon extends Vue {
        private currentPokemon: any = null;
        private message: string = "";
        private tipo_all: any = [];

        getPokemon(id: string) {
            PokemonDataService.get(id)
                .then((response) => {
                    this.currentPokemon = response.data;
                    this.currentPokemon.selected = this.currentPokemon.tipo
                    console.log(response.data);
                })
                .catch((e) => {
                    console.log(e);
                });

            PokemonDataService.getTipoAll()
                .then((response) => {
                    this.tipo_all = response.data
                    this.currentPokemon.tipo = this.tipo_all;
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        updatePokemon() {
            let pokemon = this.currentPokemon
            pokemon.tipo = this.currentPokemon.selected
            PokemonDataService.update(this.currentPokemon.id, pokemon)
                .then((response) => {
                    console.log(response.data);
                    this.currentPokemon.selected = pokemon.tipo
                    this.currentPokemon.tipo = this.tipo_all
                    this.message = "O pokemon foi atualizado com sucesso!";
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        deletePokemon() {
            PokemonDataService.delete(this.currentPokemon.id)
                .then((response) => {
                    console.log(response.data);
                    this.$router.push({ name: "pokemons" });
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        mounted() {
            this.message = "";
            this.getPokemon(this.$route.params.id);
        }
    }
</script>

<style scoped>
    .edit-form {
        max-width: 300px;
        margin: auto;
    }
</style>