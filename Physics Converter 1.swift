//contentview
import SwiftUI

struct ContentView: View {
    @State var resistance = 0.00
    @State var current = 0.00
    @State var chargeDensity = 0.00
    @State var crossSectionalArea = 0.00
    @State var driftVelocity = 0.00
    @State var voltage = 0.00
    @State var relativeChargeOfChargeCarriers = 0.00
    @State var resistivity = 0.00
    @State var lengthOfMaterial = 0.00
    
    var body: some View {
        TabView {
            ResistanceView()
                .tabItem{
                    Label("Resistance", systemImage: "person")
                }
            CurrentView()
                .tabItem {
                    Label("Current", systemImage: "pencil.tip")
                }
            VoltageView()
                .tabItem {
                    Label("Voltage", systemImage: "person")
                }
        }
    }
}

//currentview
import SwiftUI

import SwiftUI

struct CurrentView: View {
    @State var charge = 0.00
    @State var time = 0.00
    @State var resistance = 0.00
    @State var current = 0.00
    @State var current2 = 0.00
    @State var current3 = 0.00
    @State var chargeDensity = 0.00
    @State var crossSectionalArea = 0.00
    @State var driftVelocity = 0.00
    @State var voltage = 0.00
    @State var relativeChargeOfChargeCarriers = 0.00
    @State var resistivity = 0.00
    @State var lengthOfMaterial = 0.00
    var body: some View {
        ScrollView {
            Text("Current unknown (I = nAvq)")
                .font(.title)
            TextField("Charge density of material", value: $chargeDensity, format: .number)
                .textFieldStyle(.roundedBorder)
            TextField("Drift velocity of charge carriers", value: $driftVelocity, format: .number)
                .textFieldStyle(.roundedBorder)
            TextField("Cross-sectional area", value: $crossSectionalArea, format: .number)
                .textFieldStyle(.roundedBorder)
            TextField("Relative charge of charge carriers", value: $relativeChargeOfChargeCarriers, format: .number)
                .textFieldStyle(.roundedBorder)
            let current = chargeDensity*crossSectionalArea*driftVelocity*relativeChargeOfChargeCarriers
            HStack{
                Text("Current is")
                Text(String(current))
                    .bold()
                Text("A")
                    .bold()
            }
            VStack{
                Text("Current unknown (I = V/R)")
                    .font(.title)
                    .padding()
                    .padding()
                TextField("Voltage across component", value: $voltage, format: .number)
                    .textFieldStyle(.roundedBorder)
                TextField("Resistance of component", value: $resistance, format: .number)
                    .textFieldStyle(.roundedBorder)
                let current2 = voltage/resistance
                HStack {
                    Text("Current is")
                    Text(String(current2))
                        .bold()
                    Text("A")
                        .bold()
                }
            }
            VStack {
                Text("Current unknown (I = Q/t)")
                    .font(.title)
                    .padding()
                    .padding()
                TextField("Charge travelled through a point in the circuit", value: $charge, format: .number)
                    .textFieldStyle(.roundedBorder)
                TextField("Time taken", value: $time, format: .number)
                    .textFieldStyle(.roundedBorder)
                let current3 = charge/time
                HStack{
                    Text("Current is")
                    Text(String(current3))
                        .bold()
                    Text("A")
                        .bold()
                }
            }
        }
    }  
}
//resistanceview
import SwiftUI

import SwiftUI

struct ResistanceView: View {
    @State var resistance = 0.00
    @State var resistance2 = 0.00
    @State var current = 0.00
    @State var chargeDensity = 0.00
    @State var crossSectionalArea = 0.00
    @State var driftVelocity = 0.00
    @State var voltage = 0.00
    @State var relativeChargeOfChargeCarriers = 0.00
    @State var resistivity = 0.00
    @State var lengthOfMaterial = 0.00
    var body: some View {
        ScrollView {
            Text("Resistance unknown (R = pL/A)")
                .font(.title)
            TextField("Resistivity", value: $resistivity, format: .number)
                .textFieldStyle(.roundedBorder)
            TextField("Length", value: $lengthOfMaterial, format: .number)
                .textFieldStyle(.roundedBorder)
            TextField("Cross-sectional area", value: $crossSectionalArea, format: .number)
                .textFieldStyle(.roundedBorder)
            let resistance = resistivity*lengthOfMaterial/crossSectionalArea
            HStack {
                Text("Resistance is")
                Text(String(resistance))
                    .bold()
                Text("Ω")
                    .bold()
            }
            
            Text("Resistance unknown (R = V/I)")
                .font(.title)
                .padding()
                .padding()
            TextField("Voltage across component", value: $voltage, format: .number)
                .textFieldStyle(.roundedBorder)
            TextField("Current across component", value: $current, format: .number)
                .textFieldStyle(.roundedBorder)
            let resistance2 = voltage/current
            HStack {
                Text("Resistance is")
                Text(String(resistance2))
                    .bold()
                Text("Ω")
                    .bold()
            }
        }
    }  
}
//voltageview
import SwiftUI

import SwiftUI

struct VoltageView: View {
    @State var charge = 0.00
    @State var time = 0.00
    @State var resistance = 0.00
    @State var current = 0.00
    @State var current2 = 0.00
    @State var current3 = 0.00
    @State var chargeDensity = 0.00
    @State var crossSectionalArea = 0.00
    @State var driftVelocity = 0.00
    @State var voltage = 0.00
    @State var relativeChargeOfChargeCarriers = 0.00
    @State var resistivity = 0.00
    @State var lengthOfMaterial = 0.00
    var body: some View {
        ScrollView {
            Text("Voltage unknown (V = IR)")
                .font(.title)
            TextField("Current across component", value: $current, format: .number)
                .textFieldStyle(.roundedBorder)
            TextField("Resistance of component", value: $resistance, format: .number)
                .textFieldStyle(.roundedBorder)
            let voltage = resistivity*lengthOfMaterial/crossSectionalArea
            HStack {
                Text("Resistance is")
                Text(String(resistance))
                    .bold()
                Text("Ω")
                    .bold()
            }
        }
    }
}

