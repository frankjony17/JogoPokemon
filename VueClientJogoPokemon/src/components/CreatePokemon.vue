<template>
    <div class="submit-form">
        <div v-if="!submitted">
            <div class="form-group">
                <label for="name">Nome</label>
                <input
                        type="text"
                        class="form-control"
                        id="name"
                        required
                        v-model="pokemon.name"
                        name="name"
                />
            </div>
            <div class="form-group">
                <label for="tamanho">Tamanho</label>
                <input
                        type="text"
                        class="form-control"
                        id="tamanho"
                        required
                        v-model="pokemon.tamanho"
                        name="tamanho"
                />
            </div>
            <div class="form-group">
                <label for="ordem">Ordem</label>
                <input
                        class="form-control"
                        id="ordem"
                        required
                        v-model="pokemon.ordem"
                        name="ordem"
                />
            </div>
            <div class="form-group">
                <label for="tipo">Tipo</label>
                <select class="form-control"
                        v-model="pokemon.selected"
                        id="tipo"
                        required
                        name="tipo"
                >
                    <option v-for="tipo in pokemon.tipo" v-bind:value="tipo">
                        {{ tipo.name }}
                    </option>
                </select>
            </div>
            <button @click="savePokemon" class="btn btn-success">Enviar</button>
        </div>

        <div v-else>
            <h4>Você enviou com sucesso!</h4>
            <button class="btn btn-success" @click="newPokemon">Adicionar</button>
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from "vue-property-decorator";
    import PokemonDataService from "../services/PokemonDataService";

    @Component
    export default class CreatePokemon extends Vue {
        private pokemon: any = {
            id: null,
            name: "",
            tamanho: 0,
            ordem: "false",
            tipo: [],
            selected: ""
        };
        private tipo_all: any = [];
        private submitted: boolean = false;

        savePokemon() {
            console.log(this.pokemon.selected)
            let data = {
                name: this.pokemon.name,
                tamanho: this.pokemon.tamanho,
                ordem: this.pokemon.ordem,
                tipo: this.pokemon.selected
            };

            PokemonDataService.create(data)
                .then((response) => {
                    this.pokemon.id = response.data.id;
                    this.submitted = true;
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        getTipo() {
            PokemonDataService.getTipoAll()
                .then((response) => {
                    this.tipo_all = response.data
                    this.pokemon.tipo = this.tipo_all;
                })
                .catch((e) => {
                    console.log(e);
                });
        }

        newPokemon() {
            this.submitted = false;
            this.pokemon = {};
            this.pokemon.tipo = this.tipo_all;
        }

        mounted() {
            this.getTipo()
        }
    }
</script>

<style scoped>
    .submit-form {
        max-width: 300px;
        margin: auto;
    }
</style>