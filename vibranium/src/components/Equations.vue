<template>
    <div id="app">
        <h1>Equation Solver</h1>
        <v-app id="inspire">
            <v-form>
                <v-container>
                    <v-layout row wrap>
                        <v-flex xs12 sm6 md3 offset-sm2>
                            <v-text-field
                                    label="Left side"
                                    outline
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 sm6 md3 offset-sm2>
                            <v-text-field
                                    label="Right side"
                                    outline
                            ></v-text-field>
                        </v-flex>



                    </v-layout>
                    <v-app id="inspire">
                        <div>
                            <v-btn color="success">Balance</v-btn>
                        </div>
                    </v-app>
                </v-container>
            </v-form>
        </v-app>
    </div>
</template>
<style>
    h1{
        padding:10px
    }
</style>

