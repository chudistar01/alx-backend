import { createQueue } from 'kue';

const queue = createQueue();

/**
 * sends notification to specified user
 * @param {string} PhoneNumber - phonenumber
 * @param {string} Message - message
 */
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.PhoneNumber, job.data.message);
    done();
});
