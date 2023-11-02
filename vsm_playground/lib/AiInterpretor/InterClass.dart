class InterClass {
  Map<String, String> interKeys = {
    'Add Product': 'addProductScreen',
    'Edit Interface': 'interfacePage',
  };

  translateKey(String key) {}

  createCustomApp() {
    //Generate Banner Image prompt
    //First create Generate color scheme
    //Get prompts for product images
    //Get Product map
    //Generate Structure of app
    // Combine
  }

  parseCommand(String value) {
    String command = value.split(":")[0];
    switch (command) {
      case "<nav":
        navigate(value.split(":")[1]);
        break;
      case "<sm":
        shopMgmnt(value.split(":")[1]);
      default:
    }
  }

  navigate(String channel) {
    String destination = channel.split(">")[0];
    switch (destination) {
      case "Dashboard":
        break;
      case "AddProduct":
        break;
      default:
    }
  }

  shopMgmnt(String channel) {
    String method = channel.split(":")[0];
    switch (method) {
      case "addProduct":
        break;
      case "changeThemeColor":
        break;
      default:
    }
  }
}
