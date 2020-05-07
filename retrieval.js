let userRef = db.collection('users').doc('user1');
let getDoc = cityRef.get()
    .then(doc => {
        if(!doc.exists){
            console.log('No such document!');
        } else {
            console.log('Document Data: ',doc.data());
        }
    })
    .catch(err => {
        console.log('Error getting document',err);
    })

db.collection("users")
.doc("user1")
.get()
.then(doc => {
    console.log(doc.data())
})