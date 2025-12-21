import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => {
    return results.map((result) => {
      const obj = {};
      obj.status = result.status;
      obj.value = result.reason !== undefined ? result.reason : result.value;
      return obj;
    });
  });
}
