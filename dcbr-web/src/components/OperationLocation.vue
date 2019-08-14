<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <!-- <v-card-title primary-title>
        <h2>Operation Location(s)</h2>
      </v-card-title>-->
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!-- Home address section  -->

              <v-layout row mt-3 mx-2>
                <h4>Address {{number}}</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetNumber"
                    :rules="streetNumberRules"
                    label="Street number"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="aptNumber" label="Apt/Suite" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetName"
                    :rules="nameRules"
                    label="Street name"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field v-model="city" :rules="nameRules" label="City" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="postalCode"
                    :rules="nameRules"
                    label="Postal Code"
                    required
                  ></v-text-field>
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
  props: ["number"],
  data: () => ({
    valid: false,
    aptNumber: "",
    streetName: "",
    postalCode: "",
    city: "",
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    streetNumber: "",
    streetNumberRules: [v => !!v || "Street number is required"]
  }),
  methods: {}
};
</script>
