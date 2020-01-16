<template>

  <b-container fluid class="main">
    <div class="header-side">
      <b-row align-v="center" class="header">
        <b-col cols="6" md="4" class="text-center"><h3>My Currnet :  <b-badge>Jobs</b-badge></h3></b-col>
        <b-col cols="6" md="4"></b-col>
        <b-col cols="6" md="4">
          <b-button size="lg" @click="$router.push('dbselect')" style="font-size:16px;">
              <b-row align-v="center">
                <b-col cols="1" md="1" class="text-center">
                  <v-icon name="plus" style="height:20px; width:20px;"></v-icon>
                </b-col>
                <b-col cols="9" md="9" class="text-center">
                  Create A Job
                </b-col>
               </b-row>
          </b-button>
        </b-col>
      </b-row>
    </div>
    <b-row>
      <b-col sm="5" md="6" class="my-1">
        <b-form-group
          label="Per page"
          label-cols-sm="6"
          label-cols-md="4"
          label-cols-lg="3"
          label-align-sm="right"
          label-size="sm"
          label-for="perPageSelect"
          class="mb-0"
        >
          <b-form-select
            v-model="perPage"
            id="perPageSelect"
            size="sm"
            :options="pageOptions"
          ></b-form-select>
        </b-form-group>
      </b-col>

      <b-col sm="7" md="6" class="my-1">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          align="fill"
          size="sm"
          class="my-0"
        ></b-pagination>
      </b-col>
    </b-row>

    <!-- Main table element -->
    <b-table
      show-empty
      small
      stacked="md"
      :items="items"
      :fields="fields"
      :current-page="currentPage"
      :per-page="perPage"
      :filter="filter"
      :filterIncludedFields="filterOn"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      :sort-direction="sortDirection"
      @filtered="onFiltered"
    >
      <template v-slot:cell(name)="row">
        {{ row.value }}
      </template>

      <template v-slot:cell(actions)="row">
        <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">
          Info Job
        </b-button>
        <b-button size="sm" @click="$router.push('convert')">
          {{ row.detailsShowing ? 'Hide' : 'Show' }} Details
        </b-button>
      </template>

      <template v-slot:row-details="row">
        <b-card>
          <ul>
            <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
          </ul>
        </b-card>
      </template>
    </b-table>
    <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
      <pre>{{ infoModal.content }}</pre>
    </b-modal>
  </b-container>

</template>

<script>
  export default {
    data() {
      return {
        items: [
          { isActive: true, jobstatus: 'Progressing', name: 'First Job'},
          { isActive: false, jobstatus: 'Completed', name: 'Second Job' },
          {
            isActive: false,
            jobstatus: 'Progressing',
            name: 'Third Job',
            _rowVariant: 'success'
          },
          { isActive: false, jobstatus: 'Ready', name: 'Fourth Job'},
          { isActive: true, jobstatus: 'Progressing', name: 'Fifth Job' },
          { isActive: false, jobstatus: 'Completed', name: 'Sixth Job' },
          { isActive: true, jobstatus: 'Progressing', name: 'Seventh Job' },
          {
            isActive: true,
            jobstatus: 'progressing',
            name: 'Eighth Job',
          },
          { isActive: false, jobstatus: 'Progressing', name: 'Ninth Job' },
          { isActive: false, jobstatus: 'Ready', name: 'Tenth Job'  },
          { isActive: true, jobstatus: 'Completed', name: 'Eleventh Job' },
          { isActive: false, jobstatus: 'Ready', name: 'Twelveth Job' }
        ],
        fields: [
          { key: 'name', label: 'My Jobs', sortable: true, sortDirection: 'desc' },
          { key: 'jobstatus', label: 'Job Status', sortable: true, class: 'text-center' },
          {
            key: 'isActive',
            label: 'is Active',
            formatter: (value, key, item) => {
              return value ? 'Yes' : 'No'
            },
            sortable: true,
            sortByFormatted: true,
            filterByFormatted: true
          },
          { key: 'actions', label: 'Actions' }
        ],
        totalRows: 1,
        currentPage: 1,
        perPage: 5,
        pageOptions: [5, 10, 15],
        sortBy: '',
        sortDesc: false,
        sortDirection: 'asc',
        filter: null,
        filterOn: [],
        infoModal: {
          id: 'info-modal',
          title: '',
          content: ''
        }
      }
    },
    computed: {
      sortOptions() {
        // Create an options list from our fields
        return this.fields
          .filter(f => f.sortable)
          .map(f => {
            return { text: f.label, value: f.key }
          })
      }
    },
    mounted() {
      // Set the initial number of items
      this.totalRows = this.items.length
    },
    methods: {
      info(item, index, button) {
        this.infoModal.title = `Row index: ${index}`
        this.infoModal.content = JSON.stringify(item, null, 2)
        this.$root.$emit('bv::show::modal', this.infoModal.id, button)
      },
      resetInfoModal() {
        this.infoModal.title = ''
        this.infoModal.content = ''
      },
      onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      }
    }
  }
</script>

<style scoped>
.main {
  margin-top: 30px;
}
.header-side{
  margin:30px;
}
</style>



