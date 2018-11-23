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
                                    outline id="lhs"
                            ></v-text-field>
                        </v-flex>
                        <v-flex xs12 sm6 md3 offset-sm2>
                            <v-text-field
                                    label="Right side"
                                    outline id="rhs"
                            ></v-text-field>
                        </v-flex>



                    </v-layout>
                    <v-app id="inspire">
                        <div>
                            <v-btn color="success" onclick="set_balanced_equation();">Balance</v-btn>
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
<script>
    set_balanced_equation = function() {
        var lhs = document.getElementById("lhs").value;
        var rhs = document.getElementById("rhs").value;
        var equation = lhs + "->" + rhs;
        xhr = new XMLHttpRequest();
        xhr.open("GET", "127.0.0.1:5000", true);
        xhr.send()
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                alert(xhr.response);
        }
    }
</script>
