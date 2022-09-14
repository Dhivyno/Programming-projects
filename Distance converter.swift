import SwiftUI

struct ContentView: View {
    @State var km = 0.00
    @State var miles = 0.00
    var body: some View {
        VStack {
            Text("Kilometres to Miles")
                .font(.title)
            HStack {
                TextField("How many Kilometres do you want to convert to Miles?", value: $km, format: .number)
                    .textFieldStyle(.roundedBorder)
                Text(String(km*0.62137))
                    
            }
            Text("Miles to Kilometres")
                .font(.title)
            HStack {
                TextField("How many Miles do you want to convert to Kilometres?", value: $km, format: .number)
                    .textFieldStyle(.roundedBorder)
                Text(String(km/0.62137))
        }
        }
    }
}
