import http from "../http-common";

class PokemonDataService {
    getAll() {
        return http.get("/pokemon/find/all");
    }

    get(id: string) {
        return http.get('/pokemon/find/' + id);
    }

    create(data: any) {
        return http.post("/pokemon/create", data);
    }

    update(id: string, data: any) {
        return http.put('/pokemon/update/' + id, data);
    }

    delete(id: string) {
        return http.delete("/pokemon/delete/" + id);
    }

    deleteAll() {
        return http.delete("/pokemon/remove/all");
    }

    findByName(nome: string) {
        return http.get("/pokemon?nome=" + nome);
    }

    getTipoAll() {
        return http.get("/pokemon/tipo/find/all");
    }
}

export default new PokemonDataService();