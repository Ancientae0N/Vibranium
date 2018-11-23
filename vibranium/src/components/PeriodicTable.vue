<template>
<v-layout row wrap>
  <v-flex xs12>
    <h1>Vue isotope</h1>
  </v-flex>
  <v-flex xs12>
    <h2>Filter</h2>
    <div class="button-group">
      <v-btn v-for="(val, key) in option.getFilterData" :class="[key===filterOption? 'is-checked' : '']" @click="$refs.isotope.filter(key)">{{key}}
      </v-btn>
    </div>
    Filter Text<v-input type='text' v-model="filterText"></v-input>
  </v-flex>
  <v-flex xs12>
    <h2>Sort</h2>
    <div class="button-group">
      <v-btn class='md-raised' :class="[sortOption==='original-order'? 'is-checked' : '']" @click="$refs.isotope.sort('original-order')">original order</v-btn>
      <v-btn class='md-raised' v-for="(val, key) in option.getSortData" :class="[key===sortOption? 'is-checked' : '']" @click="$refs.isotope.sort(key)">{{key}}</v-btn>
    </div>
  </v-flex>
  <v-flex xs12>
    <v-slider min='100' max='1000' v-model="currentTemperature"></v-slider>
    {{currentTemperature}}
  </v-flex>
  <v-flex xs12>
    <isotope style="margin-top:50px" ref="isotope" id="root_isotope1" :list="list" :options='option' @filter="filterOption=arguments[0]" @sort="sortOption=arguments[0]">
      <div v-for="(element,index) in list" :key="index">
        <router-link :to="'/element/'+String(element.symbol).toLowerCase()">
          <v-card class="card" style="width:150px">
            <v-card-title>
              {{element.symbol}}
            </v-card-title>
            {{element.name}}<br />
            {{element.number}}<br />
            {{element.weight}}
            <v-card-actions>
            </v-card-actions>
          </v-card>
        </router-link>
      </div>
    </isotope>
  </v-flex>
</v-layout>
</template>

<script>
import data from "./periodic_table.js";
import isotope from 'vueisotope';

var baddata = [{
    name: "Mercury",
    symbol: "Hg",
    number: 80,
    weight: 200.59,
    category: "transition",
    metal: true
  },
  {
    name: "Tellurium",
    symbol: "Te",
    number: 52,
    weight: 127.6,
    category: "metalloid"
  },
  {
    name: "Bismuth",
    symbol: "Bi",
    number: 83,
    weight: 208.980,
    category: "post-transition",
    metal: true
  },
  {
    name: "Lead",
    symbol: "Pb",
    number: 82,
    weight: 207.2,
    category: "post-transition",
    metal: true
  },
  {
    name: "Gold",
    symbol: "Au",
    number: 79,
    weight: 196.967,
    category: "transition",
    metal: true
  },
  {
    name: "Potassium",
    symbol: "K",
    number: 19,
    weight: 39.0983,
    category: "alkali",
    metal: true
  },
  {
    name: "Sodium",
    symbol: "Na",
    number: 11,
    weight: 22.99,
    category: "alkali",
    metal: true
  },
  {
    name: "Cadmium",
    symbol: "Cd",
    number: 48,
    weight: 112.411,
    category: "transition",
    metal: true
  },
  {
    name: "Calcium",
    symbol: "Ca",
    number: 20,
    weight: 40.078,
    category: "alkaline-earth",
    metal: true
  },
  {
    name: "Rhenium",
    symbol: "Re",
    number: 75,
    weight: 186.207,
    category: "transition",
    metal: true
  },
  {
    name: "Ytterbium",
    symbol: "Yb",
    number: 70,
    weight: 173.054,
    category: "lanthanoid"
  },
  {
    name: "Fucktard",
    //symbol: "Fc",
    //number: 70,
    //weight: 173.054,
    //category: "lanthanoid"
  }
]

console.log(data);
export default {
  components: {
    isotope
  },
  data: function() {
    var _this = this;
    return {
      currentTemperature: '',
      currentLayout: "masonry",
      filterText: '',
      list: baddata,
      selected: null,
      sortOption: "original-order",
      filterOption: "metal",
      option: {
        filter: 'metal',
        getFilterData: {
          "show all": function() {
            return true;
          },
          metal: function(el) {
            return !!el.metal;
          },
          transition: function(el) {
            return el.category === "transition";
          },
          "alkali and alkaline-earth": function(el) {
            return el.category === "alkali" || el.category === "alkaline-earth";
          },
          "not transition": function(el) {
            return el.category !== "transition";
          },

          "metal but not transition": function(el) {
            return !!el.metal && el.category !== "transition";
          },
          "number > 50": function(el) {
            return el.number > 50;
          },
          "name ends with ium": function(el) {
            return el.name.match(/ium$/);
          },
          filterByText: function(itemElem) {
            return itemElem.name.toLowerCase().includes(_this.filterText.toLowerCase());
          }
        },
        getSortData: {
          name: "name",
          symbol: "symbol",
          number: "number",
          weight: "weight",
          category: "category"
        },
        cellsByRow: {
          columnWidth: 220,
          rowHeight: 220
        },
        masonryHorizontal: {
          rowHeight: 110
        },
        cellsByColumn: {
          columnWidth: 220,
          rowHeight: 220
        },
        packery: {
          gutter: 10
        }
      }
    }
  }
};
</script>

<style>
.col: {
  width: 80%
}

.md-card: {
  width: 40px
}
</style>
