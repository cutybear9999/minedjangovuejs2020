<template>
  <b-container fluid class="main">
    <form @submit.prevent ="submitserver">
        <div id="dbselect">
              <b-row align-h="around">
                <b-col cols="4">
                    <b-card class="mt-3" header="Oracle">
                        <b-form-group label="Select Database">
                          <b-form-radio class="frmradio" v-model="selected" name="oracle-radios" value="A">From Dumped File(*.sql)</b-form-radio>
                          <b-form-file
                            class="frmfile"
                            v-model="file"
                            :state="Boolean(file)"
                            placeholder="Choose a file or drop it here..."
                            drop-placeholder="Drop file here..."
                          ></b-form-file>
                          <b-form-radio class="frmradio" v-model="selected" name="oracle-radios" value="B">From Server</b-form-radio>
                          <b-card class="mt-3" header="Oracle server">
                              <b-row >
                                <b-col sm="3">
                                  <label class="orlitem">Host :</label>
                                </b-col>
                                <b-col sm="9">
                                  <input class="orlitem" v-model="dbFormData.orlHost"> </input>
                                </b-col>
                                <b-col sm="3">
                                  <label class="orlitem">Port :</label>
                                </b-col>
                                <b-col sm="9">
                                  <input class="orlitem" type="text" v-model="dbFormData.orlPort"></input>
                                </b-col>
                                <b-col sm="3">
                                  <label class="orlitem">ServiceName:</label>
                                </b-col>
                                <b-col sm="9">
                                  <input class="orlitem" v-model="dbFormData.orlServiceName"> </input>
                                </b-col>
                                <b-col sm="3">
                                  <label class="orlitem">SchemaName:</label>
                                </b-col>
                                <b-col sm="9">
                                  <input class="orlitem" v-model="dbFormData.orlSchemaName"> </input>
                                </b-col>
                                <b-col sm="3">
                                  <label class="orlitem">UserName :</label>
                                </b-col>
                                <b-col sm="9">
                                  <input class="orlitem" v-model="dbFormData.orlUserName"> </input>
                                </b-col>
                                <b-col sm="3">
                                  <label class="orlitem">Password :</label>
                                </b-col>
                                <b-col sm="9">
                                  <input class="orlitem" type="password" v-model="dbFormData.orlPassword"> <input>
                                </b-col>
                              </b-row>
                              <b-row align-h="around" class="frmradio">
                                <b-col cols="4" class="frmradio">
                                   <b-button variant="outline-danger">Test Connect</b-button>
                                </b-col>
                                <b-col cols="4" class="frmradio">
                                    <div class="text-center">
                                      <b-button variant="outline-secondary">
                                        Connected
                                      </b-button>
                                    </div>
                                </b-col>
                              </b-row>
                          </b-card>
                        </b-form-group>
                    </b-card>
                </b-col>

                <b-col cols="4">
                    <b-card class="mt-3" header="My SQL">
                          <b-form-group label="Select Database">
                            <b-form-radio class="frmradio" v-model="selected" name="mysql-radios" value="A">To Dumped File(*.sql)</b-form-radio>
                            <b-form-file
                              class="frmfile"
                              v-model="file"
                              :state="Boolean(file)"
                              placeholder="Choose a file or drop it here..."
                              drop-placeholder="Drop file here..."
                            ></b-form-file>
                            <b-form-radio class="frmradio" v-model="selected" name="mysql-radios" value="B">To Server</b-form-radio>
                            <b-card class="mt-3" header="My SQL server">
                                <b-row >
                                  <b-col sm="3">
                                    <label class="mysqlitem">Host :</label>
                                  </b-col>
                                  <b-col sm="9">
                                    <input class="mysqlitem" v-model="dbFormData.mysqlHost"> </input>
                                  </b-col>
                                  <b-col sm="3">
                                    <label class="mysqlitem">Port :</label>
                                  </b-col>
                                  <b-col sm="9">
                                    <input class="mysqlitem" type="text" v-model="dbFormData.mysqlPort"> </input>
                                  </b-col>
                                  <b-col sm="3">
                                    <label class="mysqlitem">DatabaseName:</label>
                                  </b-col>
                                  <b-col sm="9">
                                    <input class="mysqlitem" v-model="dbFormData.mysqlDatabaseName"> </input>
                                  </b-col>
                                  <b-col sm="3">
                                    <label class="mysqlitem">UserName :</label>
                                  </b-col>
                                  <b-col sm="9">
                                    <input class="mysqlitem" v-model="dbFormData.mysqlUserName"> </input>
                                  </b-col>
                                  <b-col sm="3">
                                    <label class="mysqlitem">Password :</label>
                                  </b-col>
                                  <b-col sm="9">
                                    <input class="mysqlitem" type="password" v-model="dbFormData.mysqlPassword"> </input>
                                  </b-col>
                                </b-row>
                                <b-row align-h="around" class="frmradio">
                                  <b-col cols="4" class="frmradio">
                                     <b-button variant="outline-danger">Test Connect</b-button>
                                  </b-col>
                                  <b-col cols="4" class="frmradio">
                                      <div class="text-center">
                                        <b-button variant="outline-secondary">
                                          Connected
                                        </b-button>
                                      </div>
                                  </b-col>
                                </b-row>
                            </b-card>
                          </b-form-group>
                    </b-card>
                </b-col>
                <b-container class="bottomside">
                  <b-row class="bottomside">
                    <b-col></b-col>
                    <b-col></b-col>
                    <b-col class="frmradio">
                        <b-row align-h="around" class="frmradio">
                          <b-col cols="4" class="frmradio">
                             <b-button class="bottombtn" variant="outline-danger" type ="submit"> Next </b-button>
                          </b-col>
                          <b-col cols="4" class="frmradio">
                              <div class="text-center">
                                <b-button variant="outline-secondary" class="bottombtn">
                                  Cancel
                                </b-button>
                                {{msg}}
                              </div>
                          </b-col>
                        </b-row>
                    </b-col>
                  </b-row>
                </b-container>
              </b-row>
        </div>
    </form>
  </b-container>

</template>

<script>
  import api from './api/index.js'
  export default {
    name:'dbselect',
    data() {
      return {
        msg:'',
        dbFormData: {
          orlHost:'',
          orlPort:'1502',
          orlServiceName:'',
          orlSchemaName:'',
          orlUserName:'',
          orlPassword:'',
          mysqlHost:'',
          mysqlPort:'3306',
          mysqlDatabaseName:'',
          mysqlUserName:'',
          mysqlPassword:''

        },

      }
    },
    methods:{
      submitserver(){
        api.fetchdbItems('post',null, this.dbFormData).then(res=>{
          this.msg = 'Saved'
        }).catch((e)=>{
        this.msg = e.response
        })
      },
    }
  }
</script>

<style>
.main, .frmradio, .frmfile{
  margin:10px;
}
.bottomside {
  margin:20px;
}
.bottombtn{
  width:120px;
}
.orlitem{
  margin : 10px;
}
.mysqlitem{
  margin : 12px;
}

.card-body .row input.orlitem{
  border: 1px solid #ddd;
  border-radius : 4px;
}

.card-body .row input.mysqlitem{
  border: 1px solid #ddd;
  border-radius : 4px;
}
</style>
