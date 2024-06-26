import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '8585858585',
  message: 'hello world'
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Notification job failed to create');
      return;
    }
    console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

