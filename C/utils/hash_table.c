typedef int (*IntHashFunction)(int);
typedef struct IntKVPair
{
    int key;
    void* value;
} IntKVPair;

typedef struct HashTable
{
    IntHashFunction hash_fn;
    IntKVPair** items;
    unsigned int size;
    unsigned int count;
} HashTable;

IntKVPair* ht_create_item(int key, void* value)
{
    IntKVPair* item = (IntKVPair*) malloc(sizeof(IntKVPair));
    item->key = key;
    item->value = value;
    return item;
}

HashTable* create_table(unsigned int size, IntHashFunction hash_fn)
{
    HashTable* table = (HashTable*) malloc(sizeof(HashTable));
    table->hash_fn = hash_fn;
    table->size = size;
    table->count = 0;
    table->items = (IntKVPair**) calloc(size, sizeof(IntKVPair*));
    for (int i=0; i<table->size; ++i)
        table->items[i] = NULL;
    return table;
}

void ht_free_item(IntKVPair* item)
{
    // Don't free item->value, since it belongs to the client
    free(item);
}

void free_table(HashTable* table)
{
    for (int i=0; i<table->size; ++i)
    {
        IntKVPair* item = table->items[i];
        if (item != NULL)
            ht_free_item(item);
    }
    free(table->items);
    free(table);
}

int ht_handle_collision(HashTable* table, IntKVPair* item)
{
    return 1;
}

int ht_put(HashTable* table, int key, void* value)
{
    if (table->count >= table->size)
    {
        printf("Error inserting into HashTable: table is full\n");
        return 1;
    }
    IntKVPair* item = ht_create_item(key, value);
    int idx = table->hash_fn(key) % table->size;
    IntKVPair current = table->items[idx];
    if (current == NULL)
    {
        table->items[idx] = item;
        table->count++;
    }
    else
    {
        if (current->key == key)
        {
            current->value = value;
            return 0;
        }
        else
        {
            int success = ht_handle_collision(table, item);
            if (success != 0)
            {
                printf("Failed to handle collision while inserting key IntKVPair into table\n");
                ht_free_item(item);
            }
            return success;
        }
    }
}

void* ht_get(HashTable* table, int key)
{
    int idx = table->hash_fn(key) % table->size;
    IntKVPair* item = table->items[idx];
    if (item != NULL && item->key == key)
        return item->value;
    return NULL;
}
