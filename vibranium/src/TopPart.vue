<template>
    <v-toolbar>
        <v-toolbar-title>Vibranium</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
            <router-link :to="'/'">
                <v-btn color="teal" flat value="recent">
                    Periodic Table
                </v-btn>
            </router-link>
            <router-link :to="'/equation'">
                <v-btn color="teal" flat value="favorites">
                    Equation
                </v-btn>
            </router-link>
            <router-link :to='"/about"'>
                <v-btn color="teal" flat value="nearby">
                    About
                </v-btn>
            </router-link>
        </v-toolbar-items>
    </v-toolbar>
</template>
