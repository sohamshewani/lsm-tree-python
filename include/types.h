```c
#ifndef TYPES_H
#define TYPES_H

// Define data types and constants

// Key and value types
enum { KEY_TYPE_STRING, KEY_TYPE_INTEGER, KEY_TYPE_FLOAT, KEY_TYPE_BINARY } key_type_t;
enum { VALUE_TYPE_STRING, VALUE_TYPE_INTEGER, VALUE_TYPE_FLOAT, VALUE_TYPE_BINARY } value_type_t;

// Define a basic key structure
struct Key {
    int64_t timestamp;
    key_type_t type;
    union {
        char *string_val;
        int64_t integer_val;
        float float_val;
        char *binary_val;
    } value;
};

// Define a basic value structure
struct Value {
    value_type_t type;
    union {
        char *string_val;
        int64_t integer_val;
        float float_val;
        char *binary_val;
    } value;
};

// Define the types of log operations
enum { WRITE, UPDATE, DELETE } log_operation_t;

// Define the types of merge operations
enum { MERGE, NO_MERGE } merge_operation_t;

// Define the types of bloom filter types
enum { KEY_BLOOM, KEY_VALUE_BLOOM } bloom_filter_type_t;

#endif
