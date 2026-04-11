function displayMessage(print_STDOUT) {
  process.stdout.write(print_STDOUT);
    process.stdout.write("\n");
}
module.exports = displayMessage ;
