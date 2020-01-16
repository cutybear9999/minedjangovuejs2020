<template>
<b-container fluid class="main">
      <div class="tree-table container">
        <h2>Tables & Views & Stored Procedures</h2>
          <vue-ads-table :columns="columns" :rows="rows"></vue-ads-table>
      </div>
      <b-form-textarea
        id="textarea"
        v-model="text"
        placeholder="Enter something..."
        rows="3"
        max-rows="6"
      ></b-form-textarea>

      <div class="main">
         <b-row>
          <b-col></b-col>
          <b-col><b-button variant="outline-success">Save</b-button></b-col>
          <b-col>
            <b-button variant="outline-primary" class="btnbottom" @click="$router.push('createjob')">  Next </b-button>
            <b-button variant="outline-secondary" class="btnbottom" @click="$router.push('tbcheck')"> Back </b-button>
          </b-col>
        </b-row>
      </div>
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
        text:'',
        rows,
        columns,
      };
    },
};
</script>

<style>
#textarea{
  margin:30px auto;
  width:59%;
  height:300px;
}
.main{
  margin:30px auto;
}

</style>

