<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Animal Identification</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!--OPERATION DETAILS-NAME  -->

              <!-- Type of Operator -->
              <v-layout mx-2 mt-4>
                <subheader>Do you maintain a permanent identification of your animals?</subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="hasId" row>
                  <v-radio label="Yes" value="true"></v-radio>
                  <v-radio label="No" value="false"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- Type of Animal -->
              <v-layout mx-2 mt-4>
                <subheader>What type of identification technology do you use?</subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="idType" row>
                  <v-radio label="Microchip" value="MICROCHIP"></v-radio>
                  <v-radio label="Tattoo" value="TATTOO"></v-radio>
                  <v-radio label="Other" value="OTHER"></v-radio>
                </v-radio-group>
              </v-layout>
              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field v-model="otherId" label="Other Method"></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    hasId: null,
    idType: null,
    otherId: "",

    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    email: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ]
  })
};
</script>
