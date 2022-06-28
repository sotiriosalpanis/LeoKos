import Link from 'next/link'
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
              <Link
              key={trip._id}
              href={`/trips/${trip._id}`}
              >
                <h3>{trip.trip_name}</h3>
              </Link>
             
            ))}
          </div>
      </main>
    </div>
  )
}
