//  import uploadPhoto and createUser from utils.js
import { uploadPhoto, createUser } from './utils.js';

export default async function handleProfileSignup() {
  try {
    const [photo, user] = await Promise.all([uploadPhoto(), createUser()]);
    console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  } catch {
    console.log('Signup system offline');
  }
}