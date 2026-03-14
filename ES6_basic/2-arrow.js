export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods =;

  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}
