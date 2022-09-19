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
                    Label("Resistance Unknown", systemImage: "person")
                }
            CurrentView()
                .tabItem {
                    Label("Current Unknown", systemImage: "pencil.tip")
                }
            }
        }
    }
//currentview
import SwiftUI

import SwiftUI

struct CurrentView: View {
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
        ScrollView {
            Text("Current unknown (I = nAvq)")
                .font(.title)
            TextField("Charge density of material", value: $chargeDensity, format: .number)
            TextField("Drift velocity of charge carriers", value: $driftVelocity, format: .number)
            TextField("Cross-sectional area", value: $crossSectionalArea, format: .number)
            TextField("Relative charge of charge carriers", value: $relativeChargeOfChargeCarriers, format: .number)
        }
    }  
}
//resistanceview
import SwiftUI

import SwiftUI

struct ResistanceView: View {
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
        ScrollView {
            Text("Resistance unknown")
                .font(.title)
            
            TextField("Resistivity", value: $resistivity, format: .number)
            TextField("Length", value: $lengthOfMaterial, format: .number)
            TextField("Cross-sectional area", value: $crossSectionalArea, format: .number)
        }
    }  
}

