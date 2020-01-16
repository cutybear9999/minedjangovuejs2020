
<template>

<b-container fluid class="main">
    <div class="head-section">
      <b-row class="text-center">
        <b-col></b-col>
          <b-col cols="8">
            <b-col sm="2">
            <label for="input-default"><h2>Job Name</h2></label>
          </b-col>
          <b-col sm="10">
            <b-form-input id="input-name" placeholder="Enter your name"></b-form-input>
          </b-col>
        </b-col>
        <b-col></b-col>
      </b-row>

      <b-row class="text-center">
        <b-col></b-col>
          <b-col cols="8">
            <b-col sm="2">
            <label for="input-default"><h2>Schema</h2></label>
          </b-col>
          <b-col sm="10">
            <b-form-select id ="input-opt" v-model="selected" :options="options"></b-form-select>
          </b-col>
        </b-col>
        <b-col></b-col>
      </b-row>
    </div>

    <div class="tree-table container">
         <vue-ads-table :columns="columns" :rows="rows"></vue-ads-table>
     </div>

      <b-row class="bottomside">
        <b-col></b-col>
        <b-col class="frmradio">
            <b-row align-h="around" class="frmradio">
              <b-col cols="4" class="frmradio">
                 <b-button variant="outline-secondary" class="bottombtn" @click="$router.push('dbselect')">Back</b-button>
              </b-col>
              <b-col cols="4" class="frmradio">
                  <div class="text-center">
                    <b-button class="bottombtn" variant="outline-danger" @click="$router.push('tbview')">
                      Next
                    </b-button>
                  </div>
              </b-col>
            </b-row>
        </b-col>
        <b-col></b-col>
      </b-row>
</b-container>
</template>

<script type = "text/javascript">
import { VueAdsTable } from 'vue-ads-table-tree';

export default {
    name: 'TreeTable',
    components: {
        VueAdsTable,
    },
    data() {
        item:"Here it is ...."
        const rows = [
          {
            id: 'Tables',
            name: '',
            city: '',
            _children: [
              {
                id: 'table1',
                name: 'item-1',
                city: 'item-1',
              },
              {
                id: 'table2',
                name: 'item-2',
                city: 'item-2',
              },
              {
                id: 'table3',
                name: 'item-3',
                city: 'item-3',
              },
            ],
          },
          {
            id: 'Views',
            name: '',
            _children: [
              {
                id: 'View1',
                name: 'item-1',
                city: 'item-1',
              },
              {
                id: 'View2',
                name: 'item-2',
                city: 'item-2',
              },
            ],
          },
          {
            id: 'Stored Procedures',
            city: '',
            _children: [
              {
                id: 'Procedure1',
                name: 'item-1',
                city: 'item-1',
                _children: [
                  {
                    id: 'Procedure1-1-1',
                    name: 'item-1-1',
                    city: 'item-1-1',
                  },
                ],
              },
            ],
          },
          {
            id: 'Etc',
            name: 'etc item-1',
            city: 'etc item-2',
          },
        ];

        const columns = [
          {
            property: 'id',
            title: 'Root',
            collapseIcon: true,
          },
          {
            property: 'name',
            title: 'item1',
          },
          {
            property: 'city',
            title: 'item2',
            filterble: true,
          },
        ];

        return {
          rows,
          columns,
          options: [
            { value: null, text: 'Please select an option' },
            { value: 'a', text: 'This is First option' },
            { value: 'b', text: 'Selected Option' },
            { value: { C: '3PO' }, text: 'This is an option with object value' },
            { value: 'd', text: 'This one is disabled', disabled: true }
          ]
        };
  },
};
</script>

<style>
.main{
  margin:30px auto;
}
.my-1{
  margin:20px auto;
}
.head-section{
  padding-left:150px;
  padding-bottom:50px;
}

bottomside{

}

</style>
