new Vue({
  el: "#app",
  data() {
    return {
      PrescriptionMedicine:[],
      PrescriptionMedicineForm :{
        medicine_name :'',
        medicine_duration:[],
        duration:'',
        duration_type:'',
        remarks:'',
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

    },
    GetMadicineData:function() {
        const _this = this;
        axios.get()
        .then((response) => {

        })
        .catch((error) => {
          
        })
    },
    AddNewMedicineForm:function() {
      const _this = this;
      _this.PrescriptionMedicine.push(_this.PrescriptionMedicineForm);
      console.log(_this.PrescriptionMedicineForm);
    },
    RemoveMedicineForm:function( index ) {
       const _this = this ;
	     _this.PrescriptionMedicine.splice(index,1)
    }
  },
  created() {
    console.log("okdsds")
  }
});
