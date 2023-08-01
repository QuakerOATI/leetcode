export default class Dict {
    constructor(keyToString, stringToKey) {
        this.keyToString = keyToString;
        this.stringToKey = stringToKey;
        this.dict = {};
    }
    set(key, value) {
        this.dict[this.keyToString(key)] = value;
    }
    get(key) {
        return this.dict[this.keyToString(key)];
    }
    has(key) {
        return this.dict.hasOwnProperty(this.keyToString(key));
    }
    *items() {
        yield* Object.entries(this.dict).map(([k, v]) => [this.stringToKey(k), v]);
    }
    *keys() {
        yield* Object.keys(this.dict).map(this.stringToKey);
    }
    *values() {
        yield* Object.values(this.dict).map(this.stringToKey);
    }
}

