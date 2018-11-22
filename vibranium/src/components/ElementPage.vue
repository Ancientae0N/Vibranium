<template>
  <div class="container">
    <base href="https://raw-dot-custom-elements.appspot.com/FlorianFe/chemical-element-visualisation/v1.0.4/chemical-element-visualisation/">
    <link rel="import" href="chemical-element-visualisation.html">
    <header>

    </header>

    <table width="25%" style="position: absolute; top: 40px;">
      <tr>
        <td><chemical-element-visualisation symbol="fe" tooltip="false"></chemical-element-visualisation></td>
      </tr>
    </table>

    <table width="50%" border="1" style="position: absolute; top: 50px; left: 27.5%;">
      <thead>
      <td>Property</td>
      <td>Value</td>
      </thead>
      <tr>
        <td>Electronic Configuration</td>
        <td>1s2 2s2 2p2</td>
      </tr>
    </table>

    <table width="15%" style="position: absolute; top: 30px; left: 80%; background: red; text-align: center;">
      <tr>
        <td style="font-size: 35px;">
          C
        </td>
      </tr>
      <tr>
        <td>Carbon</td>
      </tr>
      <tr>
        <td>40.8</td>
      </tr>
    </table>
    <div class="slidecontainer">
      <input type="range" min="3" max="10" value="5" class="slider" id="myRange" onchange="set_summary();">
    </div>
    <div style="position: absolute; top: 420px;">
      <p id = "summary_text"></p>
      some words in the summary
    </div>
</div>
</template>

<script>
import data from "./periodic_table.js";
import $ from 'jquery';

export default {
  name: "ElementPage",
  data() {
    return {
      elements: data
    }
  }
}
</script>

