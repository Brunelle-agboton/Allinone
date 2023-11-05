module.exports = {
    "env": {
        "browser": true,
        "node": true,
        "jest": true
    },
    "extends": [
        "eslint:recommended",
        "plugin:vue/essential",
        'plugin:jest/recommended',

    ],
    "parserOptions": {
        "ecmaVersion": 12,
        "sourceType": "module"
    },
    "plugins": [
        "vue",
        "jest"
    ],
    "rules": {
    }
};
