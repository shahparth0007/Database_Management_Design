[{
 $unwind: {
  path: '$SalesPersonInfo'
 }
}, {
 $group: {
  _id: '$Name',
  Sum: {
   $sum: '$SalesPersonInfo.TotalSales'
  }
 }
}]