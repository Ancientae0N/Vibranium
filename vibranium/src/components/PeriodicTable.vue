<template>
<v-layout row wrap>
  <v-flex xs12>
    <h1>Vue isotope</h1>
  </v-flex>
  <v-flex xs12>
    <h2>Filter</h2>
    <div class="button-group">
      <v-btn v-for="(val, key) in options.getFilterData" :class="[key===filterOption? 'is-checked' : '']" @click="$refs.isotope.filter(key)">{{key}}
      </v-btn>
    </div>
  </v-flex>
  <v-flex xs12>
    <h2>Filter Text</h2>
    <div class="button-group">
      <v-text-field label='regular'></v-text-field>
    </div>
  </v-flex>
  <v-flex xs12>
    <h2>Sort</h2>
    <div class="button-group">
      <v-btn class='md-raised' v-for="(val, key) in options.getSortData" :class="[key===sortOption? 'is-checked' : '']" @click="$refs.isotope.sort(key)">{{key}}</v-btn>
    </div>
  </v-flex>
  <v-flex xs12>
    <v-slider min='100' max='1000' v-model="currentTemperature"></v-slider>
    {{currentTemperature}}
  </v-flex>
  <v-flex xs12>
    <isotope style="margin-top:50px" ref="isotope" id="root_isotope1" :list="list" :options='options' @filter="filterOption=arguments[0]" @sort="sortOption=arguments[0]">
      <div v-for="(element,index) in list" :key="index">
        <router-link :to="'/element/'+String(element.symbol).toLowerCase()">
          <v-card class="card" style="width:150px">
            <v-card-title>
              {{element.symbol}}
            </v-card-title>
            {{element.name}}<br />
            {{element.number}}<br />
            {{element.atomic_weight}}
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
import $ from 'jquery';
import _ from 'lodash';

console.log(data);
export default {
  components: {
    isotope
  },
  mounted: function() {
    console.log("Fetching data");
    var _this = this;
    fetch('http://localhost:5000/data/all').then((d) => d.json()).then(x => _this.list = _.values(x))
  },
  data: function() {
    var _this = this;
    return {
      currentTemperature: '',
      currentLayout: "masonry",
      filterText: '',
      list: [],
      selected: null,
      sortOption: "original-order",
      filterOption: "filterByText",
      options: {
        filter: 'filterByText',
        getFilterData: {
          filterByText: function(itemElem) {
            return itemElem.name.toLowerCase().includes(_this.filterText.toLowerCase());
          }
        },
        getSortData: {
          name: "name",
          symbol: "symbol",
          atomic_number: 'atomic_number'
        },
        cellsByRow: {
          columnWidth: 230,
          rowHeight: 230
        },
        masonryHorizontal: {
          rowHeight: 110
        },
        cellsByColumn: {
          columnWidth: 220,
          rowHeight: 220
        },
        packery: {
          gutter: 20
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
