import SwiftUI

func RandomPrompt() -> String{
    let things = ["What is the apparatus needed to titrate hydrochloric acid and sodium hydroxide?"]
    return String(things.randomElement()!)
}

struct ContentView: View {
    @State var GoodThingPrompt: String = RandomPrompt()
    @State var GoodThing2: String = ""
    @State var GoodThing3: String = ""
    @State var GoodThing4: String = ""
    @State var GoodThing5: String = ""
    @State var GoodThing6: String = ""
    @State var GoodThing7: String = ""
    var body: some View {
        ScrollView {
            Text(To-Do List)
                .font(.title)
                .fixedSize(horizontal: false, vertical: true)
            TextField("Hello", text: $GoodThing2)
                .textFieldStyle(.roundedBorder)
            TextField("Hello", text: $GoodThing3)
                .textFieldStyle(.roundedBorder)
            TextField("Hello", text: $GoodThing4)
                .textFieldStyle(.roundedBorder)
            TextField("Hello", text: $GoodThing5)
                .textFieldStyle(.roundedBorder)
            TextField("Hello", text: $GoodThing6)
                .textFieldStyle(.roundedBorder)
            TextField("Hello", text: $GoodThing7)
                .textFieldStyle(.roundedBorder)
        }
    }
}
