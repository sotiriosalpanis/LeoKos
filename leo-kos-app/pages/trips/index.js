import styles from '../../styles/Home.module.css'

const tripsURL = `${process.env.DETA_ENDPOINT}trips`
const apiKey = process.env.DETA_API_KEY

export async function getStaticProps() {
  const res = await fetch(tripsURL, {
    headers : {
      'X-API-Key': apiKey
    }
  })
  const trips = await res.json()

  return {
    props: {
      trips,
    }
  }
}

export default function Trips({trips}) {

  return (
    <div className={styles.container}>

      <main className={styles.main}>
          <h1 className={styles.title}>
            Trips
          </h1>
          <div>
            {trips.map(trip => (
              <h3 key={trip._id}>{trip.trip_name}</h3>
            ))}
          </div>
      </main>
    </div>
  )
}
