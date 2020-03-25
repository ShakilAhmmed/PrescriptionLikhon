new Vue({
  el: "#app",
  data() {
    return {
      PrescriptionMedicineForm :{
        medicine_name :'',
        medicine_duration:[],
        duration:'',
        duration_type:'',

      }
    }
  },
  methods: {
    AddDuration:function( event, type ) {

      const _this = this;
      if ( event.target.checked ) {
        _this.PrescriptionMedicineForm.medicine_duration.push(type);
      } else {
          let index =_this.PrescriptionMedicineForm.medicine_duration.indexOf(type);
          if ( index > -1) {
              _this.PrescriptionMedicineForm.medicine_duration.splice(index, 1);
          }
      }
      
    }
  },
  created() {
    console.log("okdsds")
  }
});
