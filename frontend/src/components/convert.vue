

<template>
<b-container fluid class="main">
  <div><h3>Job Name : <b-badge>2019_11_26_Job1</b-badge></h3></div>
  <div>
    <b-form-textarea
      id="textarea"
      v-model="text"
      placeholder="Enter something..."
      rows="20"
      max-rows="25"
    ></b-form-textarea>

    <pre class="mt-3 mb-0">{{ text }}</pre>
  </div>
  <b-row>
      <label id="lblbar">converting...   </label>
      <b-progress :value="50" :max="max" show-progress animated id="probar"></b-progress>
  </b-row>
  <div class="main">
   <b-row>
    <b-col></b-col>
    <b-col></b-col>
    <b-col>
      <b-button variant="outline-primary" class="btnbottom" @click="$router.push('testdjango')">  Ok  </b-button>
      <b-button variant="outline-secondary" class="btnbottom" @click="$router.push('createjob')"> Cancel </b-button>
    </b-col>
  </b-row>
  </div>

</b-container>
</template>

<script>
  export default {
    data() {
      return {
        text: ''
      }
    }
  }
</script>

<style>
.main, .frmradio, .frmfile{
  margin:50px;
}
#textarea{
  width : 90%;
}
#probar{
 width : 83%;
 margin: auto 0;
 padding-left:10px;
}
#lblbar{
  font-size:20px;
  padding-left:20px;
}
.btnbottom{
  width:150px;
}

</style>
